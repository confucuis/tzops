import sys

from twisted.python import log
from twisted.internet import reactor

from zombie.config import settings
from zombie.network import ZombieFactory


ZOMBIE = r"""
@@@@@@@@@@@ @@@@@@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@@      _____
@@@@@@@@@@@ @@@@@@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@@     |>   >|
      @@@@@ @@@@   @@@@  @@@ @@@  @@@ @@@  @@@@   @@@@    @@@@    @@@@@@          \__>__/
@@@@@@@@@@@ @@@@   @@@@  @@@ @@@  @@@ @@@  @@@@@@@@@@@    @@@@    @@@@@@@@@@@       |_|
@@@@@@      @@@@   @@@@  @@@ @@@  @@@ @@@  @@@@   @@@@    @@@@    @@@@@@            |_|-{
@@@@@@@@@@@ @@@@@@@@@@@  @@@ @@@@@@@@ @@@  @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@@       |_|
@@@@@@@@@@@ @@@@@@@@@@@ @@@@ @@@@@@@@ @@@@ @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@@     ==|=|== 
"""


def main():
    # 启动服务器
    reactor.listenTCP(8000, ZombieFactory())
    log.startLogging(sys.stdout)
    print(f"Zombie Run On: {settings.app_port}")
    print(ZOMBIE)
    reactor.run()


if __name__ == "__main__":
    main()
