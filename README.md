## Voting System - Socket Programming
Implementation of a voting system (polling stations network) using a replicated dictionary. Socket Programming in Python.

A .pdf file named 'problem_description.pdf' is provided, which explains the problem in detail.

The code also handles the following two failure cases, along with the normal operations that were specified in the problem description file:

1) Network failure: Provides a way for the user to emulate network failure on server side. For network failure, an interface for close network connection is provided, such that we can close the connection between, say, A -> B by simply typing command **'networkFail'** to A's terminal. The program treats the link between the two nodes (say A->B) as failed and hence does not send any message between the two nodes. As a counterpart, there is an option to fix the network failure, again by taking user input in the corresponding server (say again A's terminal) typing command **'networkWorks'**, upon which the two nodes are be able to communicate with each other again. 

2) Server failure: In case the network fails due to server shut down, servers can resume from where the failure had happened, by storing the state of processes (logs, dictionary, and 2DTT) on disk and reading from it when the process starts back. 

**IMPORTANT: File 'initial_state_RUN_FIRST.py' must be run first to set servers initial state, and be located in the same directory as the serverX.py files.**
