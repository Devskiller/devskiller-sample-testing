# Devskiller programming task sample - Testing

## Introduction

With [DevSkiller.com](https://devskiller.com) you can assess your candidates'
programming skills as a part of your recruitment process. We have found that
programming tasks are the best way to do this and have built our tests
accordingly. The way our test works is your candidate is asked to modify the
source code of an existing project.

During the test, your candidates have the option of using our browser-based
code editor and can build the project inside the browser at any time. If they
would prefer to use an IDE they are more comfortable with, they can also
download the project code or clone the project’s Git repository and work
locally.

You can check out this short video to see the test from the [candidate's
perspective](https://devskiller.zendesk.com/hc/en-us/articles/360019534639-How-the-TalentScore-test-looks-like-from-the-candidate-perspective).

This repo contains a sample Testing project and below you can find a detailed
guide for creating your own programming project.

**Please make sure to read our [Getting started with programming
projects](https://devskiller.zendesk.com/hc/en-us/articles/360019531059-Getting-started-with-Programming-Tasks) guide first.**

## Technical details

At present, it is possible to run Testing tasks either on Ubuntu 16.04 or CentOS 7.

This task consists of three parts:

 * the initialization script `init.sh`,
 * `bats` verification tests,
 * question definition files.

The `init.sh` script is used for initializing the candidate's Virtual Machine.
You can use it to install and pre-configure all required services.

## Automatic assessment

It is possible to automatically assess the solution posted by a candidate.

**Verification tests** are unit tests that are hidden from the candidate. The
final score, calculated during verification, is a direct result of the
verification tests.

Verification tests in DevOps tasks *must* reside in the `verification`
directory, i.e. the `pathPatterns` directive in the project descriptor is ignored.

## Question definition files

In order to define a textarea field to be filled with a candidate's answer, 
you should create an empty file with a camel-cased question. 
Use underscores instead of spaces and the '.textarea.txt' suffix. 
For example, to show a "Credit card number" input field create a "Credit_card_number.textarea.txt" file.

After the test is finished, the file will contain the candidate's answer. 
You can use it in your verification tests to check the solution.

## IP address

The IP address of the server to connect to should be included in the task description using the `$vmIpAddress` placeholder.

Sample description: [README_TASK.md](README_TASK.md)

## Local development

You can verify your init.sh and verification tests using [Vagrant](https://www.vagrantup.com/).

The [Vagrantfile](Vagrantfile) is located in the root directory.


Sample scenario:

1. Provision the virtual machine using your init.sh file: `vagrant up`
2. In the Vagrantfile port 80 is forwarded to `localhost:8080`, therefore you can open it in the browser.
3. SSH into the instance: `vagrant ssh`
4. Simulate the user input: 
`echo DevSkill{SqL1_1s_5t1ll_4_th1ng_s4dly_1337} > /home/candidate/candidate-session/flag.textarea.txt`
5. Run your verification tests: `cd /home/candidate && bats verify_local`
6. Exit the virtual machine `exit`
7. Remove the provisioned virtual machine
`vagrant destroy`

## Devskiller project descriptor

Testing tasks can be configured with the Devskiller project descriptor
file:

1. Create a `devskiller.json` file.
2. Place it in the root directory of your project.

Here is an example project descriptor:

```json
{
    "verification" : {
        "testNamePatterns" : [ ".*Verification.*" ]
    }
}
```

You can find more details about the `devskiller.json` descriptor in our
[documentation](https://devskiller.zendesk.com/hc/en-us/articles/360019530419-Programming-task-project-descriptor).

## Automatic verification with verification tests

The solution submitted by the candidate may be verified using automated tests.
Simply define which tests should be treated as verification tests.

To define verification tests, you need to set configuration properties in
`devskiller.json`:

- `testNamePatterns` - an array of RegEx patterns that should match all the
  names of the verification tests.

In our sample task, all verifications tests are prefixed with the string `Verification`
In this case, the following patterns will be sufficient:

```json
"testNamePatterns" : [".*Verification.*"]
```
