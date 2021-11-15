#!/usr/bin/env bats

load 'test_helper/bats-support/load'
load 'test_helper/bats-assert/load'

@test "Verification test - check the flag" {
    run bash -c "diff --ignore-blank-lines --ignore-space-change --strip-trailing-cr $BATS_TEST_DIRNAME/../candidate-session/flag.textarea.txt $BATS_TEST_DIRNAME/flag.expected || echo 'Incorrect flag'"
    assert_output ''
}
