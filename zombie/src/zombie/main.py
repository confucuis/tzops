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
    log.startLogging(sys.stdout)
    print(ZOMBIE)
    print(f"Zombie Run On: {settings.app_port}")
    reactor.listenTCP(settings.app_port, ZombieFactory())
    reactor.run()


if __name__ == "__main__":
    main()
