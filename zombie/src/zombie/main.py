import sys

from twisted.python import log
from twisted.internet import reactor
from zombie.network import ZombieFactory


ZOMBIE = """
@@@@@@@@@@@ @@@@@@@@@@@  @@@@@@@    @@@@@@@  @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@
@@@@@@@@@@@ @@@@@@@@@@@  @@@@@@@    @@@@@@@  @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@
      @@@@  @@@     @@@  @@@ @@@    @@@ @@@  @@@     @@@    @@@@    @@@@
    @@@@    @@@     @@@  @@@  @@@  @@@  @@@  @@@@@@@@@@@    @@@@    @@@@@@@@@@
  @@@@      @@@     @@@  @@@   @@  @@   @@@  @@@     @@@    @@@@    @@@@
@@@@@@@@@@@ @@@@@@@@@@@  @@@   @@@@@@  @@@@  @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@
@@@@@@@@@@@ @@@@@@@@@@@ @@@@@  @@@@@@  @@@@@ @@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@
"""


def main():
    # 启动服务器
    reactor.listenTCP(8000, ZombieFactory())
    log.startLogging(sys.stdout)
    print("Zombie Run On: 8000")
    print(ZOMBIE)
    reactor.run()


if __name__ == "__main__":
    main()
