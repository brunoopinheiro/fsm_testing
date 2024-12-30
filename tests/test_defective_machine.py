import pytest  # noqa
from machines.defective.deadlock import DeadlockMachine
from src.fsm_tester import FSMTester


@pytest.fixture
def fsm_tester():
    return FSMTester(
        DeadlockMachine,
        dialect='pytransitions',
        final_state='Finish',
        expected_loops=1,
    )


@pytest.mark.xfail
def test_deadlock_states_suite(fsm_tester):
    suite = fsm_tester.deadlock_states_suite
    fsm_tester.run(suite)


def test_unreachable_states_suite(fsm_tester):
    suite = fsm_tester.unreachable_states_suite
    fsm_tester.run(suite)


def test_sink_states_suite(fsm_tester):
    suite = fsm_tester.sink_states_suite
    fsm_tester.run(suite)


def test_nondeterministic_transition_suite(fsm_tester):
    suite = fsm_tester.nondeterministic_transition_suite
    fsm_tester.run(suite)


def test_machine_execution_suite(fsm_tester):
    suite = fsm_tester.machine_execution_suite
    fsm_tester.run(suite)
