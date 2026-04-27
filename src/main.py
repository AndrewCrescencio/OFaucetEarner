import argparse
import asyncio
import logging
import os
import time
import random
import re
from dotenv import load_dotenv
from .client import FaucetEarnerClient
from .logger_setup import setup_logging


def normalize_cookie(cookie_input: str) -> str:
    """
    Normalizes the cookie value to always include reg=1 and login=1.

    Accepted format:
    - 132164123123
    """
    user_value = cookie_input.strip().strip('"').strip("'")
    if not user_value:
        raise ValueError("Cookie cannot be empty.")

    if not re.fullmatch(r"\d+", user_value):
        raise ValueError("COOKIE must contain only the numeric user value (example: 132164123123).")

    return f"reg=1; login=1; user={user_value}"

async def main_loop(cookie: str):
    """
    The main loop that periodically claims XRP.

    Args:
        cookie (str): The user's authentication cookie.
    """
    logging.info("Starting Faucetearner Client...")
    logging.info("Press CTRL+C to stop the program.")

    async with FaucetEarnerClient(cookie=cookie) as client:
        while True:
            try:
                start_time = time.time()

                status_message = await client.claim_xrp()
                logging.info(status_message)

                # wait_time = 600
                wait_time = random.randint(605, 610)
                logging.info(f"Will attempt the next claim in {wait_time} seconds.")

                for i in range(wait_time, 0, -1):
                    print(f"   Waiting... {i} seconds remaining   ", end='\r')
                    await asyncio.sleep(1)
                print("                                       ", end='\r')
            except asyncio.CancelledError:
                logging.info("Program stopped by user.")
                break
            except Exception as e:
                logging.error(f"An unexpected error occurred in the main loop: {e}")
                logging.info("Retrying in 60 seconds...")
                await asyncio.sleep(60)

def run():
    """
    Function to run the application from the command line.
    """
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Asynchronous bot to claim XRP tokens from Faucetearner.",
        epilog="Reads numeric COOKIE from .env by default, or accepts the numeric value as argument."
    )
    parser.add_argument(
        "cookie",
        type=str,
        nargs="?",
        default=None,
        help="Numeric Faucetearner user cookie value. Optional when COOKIE is set in .env."
    )
    args = parser.parse_args()
    cookie = args.cookie or os.getenv("COOKIE")

    if not cookie:
        parser.error("Cookie not provided. Set COOKIE in .env or pass it as an argument.")

    try:
        cookie = normalize_cookie(cookie)
    except ValueError as exc:
        parser.error(str(exc))

    setup_logging()

    try:
        asyncio.run(main_loop(cookie))
    except KeyboardInterrupt:
        logging.info("\nProcess stopped manually. Goodbye!")

if __name__ == '__main__':
    run()