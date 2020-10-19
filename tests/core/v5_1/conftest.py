import pytest

from ddht.tools.driver import Tester


@pytest.fixture
def tester():
    return Tester()


@pytest.fixture
async def alice(tester, bob):
    node = tester.node()
    node.enr_db.set_enr(bob.enr)
    return node


@pytest.fixture
async def bob(tester):
    return tester.node()


@pytest.fixture
async def driver(tester, alice, bob):
    return tester.session_pair(alice, bob)


@pytest.fixture
async def alice_network(alice, bob):
    alice.enr_db.set_enr(bob.enr)
    async with alice.network() as alice_network:
        yield alice_network


@pytest.fixture
async def bob_network(alice, bob):
    bob.enr_db.set_enr(alice.enr)
    async with bob.network() as bob_network:
        yield bob_network
