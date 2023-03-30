"""
The speed module uses speedtest and tqdm to generate internet speed test for your network.
"""

import speedtest
from time import sleep
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)


def speedTry():
    try:
        print(Fore.LIGHTMAGENTA_EX + "SEARCHING FOR BEST AVAILABLE SERVER......")

        speed = speedtest.Speedtest()

        speed.get_best_server()
        for i in tqdm(range(10), colour="green", desc="Finding Optimal Speed"):
            sleep(0.05)

        speed.download()
        for i in tqdm(range(10), colour="cyan", desc="Getting Download Speed"):
            sleep(0.05)

        speed.upload()
        for i in tqdm(range(10), colour="yellow", desc="Gettiing Upload Speed"):
            sleep(0.05)

        res_dict = speed.results.dict()

        # Assign to variables with a specific format
        dwnl = str(res_dict["download"])[:2] + "." + str(res_dict["download"])[2:4]

        upl = str(res_dict["upload"])[:2] + "." + str(res_dict["upload"])[2:4]

        # Display results
        print("\n")

        print(
            Fore.GREEN
            + f"Download: {dwnl}mbps({float(dwnl)*0.125:.2f}MBs) | Upload:{upl}mbps ({float(upl)*0.125:.2f}MBs) | Ping: {res_dict['ping']:.2f}ms".center(
                80
            )
        )
        print(Fore.MAGENTA + "-" * 100)
        print(
            Fore.CYAN
            + f"HOST:{res_dict['server']['host']} | SPONSOR:{res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f}".center(
                80
            )
        )
        print(Fore.MAGENTA + "-" * 100)

    except speedtest.ConfigRetrievalError:
        print(
            f"oh oh 🫣, It seems we are unable to conncet to a server\nTry checking your internet connection or try again later."
        )
