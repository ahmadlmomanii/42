*This activity has been created as part of the 42 curriculum by aal-moum*

# NetPractice

## Description

NetPractice is a networking project from the 42 curriculum created to practice the fundamentals of computer networks and TCP/IP addressing.

The project consists of **10 different levels**, where each level contains a network configuration that needs to be fixed. The main objective is to correctly configure IP addresses, subnet masks, gateways, router interfaces, and routing rules so that the required devices can communicate with each other.

## Instructions

1. Download and extract the NetPractice project files.
2. Open `index.html` using a web browser.
3. Enter your 42 login in the training interface.
4. Solve all **10 levels** by correcting the network configuration.
5. Click **Check again** to test whether the current configuration is valid.
6. After successfully completing a level, use **Get my config** to export the configuration.
7. Save the exported configuration before continuing to the next level.
8. Put all **10 configuration files** in the root directory of the repository.

There is no compilation or additional installation required for this project.

## Networking Concepts

During the project, I practiced and worked with several important networking concepts, including:

* IPv4 addressing
* TCP/IP networking
* Subnet masks and CIDR
* Network and host addresses
* Default gateways
* Routers and router interfaces
* Switches
* Routing tables
* OSI model

## Approach to Solving the Levels

For each level, I followed the path that a packet would take from the source device to the destination.

First, I check the IP addresses and subnet masks to determine whether the devices belong to the same network. If they are on different networks, I identify the appropriate gateway and router interfaces and then verify that the necessary routes exist.

The messages displayed by NetPractice are also useful for identifying configuration problems, such as an invalid IP address, an incorrect subnet mask, a missing gateway, or an incorrect routing entry.

## Submission

The final repository should contain the **10 configuration files**, with one exported configuration corresponding to each level.

The 42 login must be correctly entered in the NetPractice interface when generating the configuration files.

During the defense, **3 random exercises from levels 6 to 10** may be selected. They must be solved successfully within the given time limit.

External tools are not allowed during the defense, with the exception of a basic calculator such as `bc`.

## Resources

* [Cisco – Networking Basics](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-computer-networking.html)
* [Cloudflare – What is a Computer Network?](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-network/)
* [Wikipedia – Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
* [Wikipedia – OSI Model](https://en.wikipedia.org/wiki/OSI_model)
* [CCNA – Full Course](https://youtube.com/playlist?list=PLIhvC56v63IJVXv0GJcl9vO5Z6znCVb1P)

## AI Usage

ChatGPT was used as a learning assistant to understand networking concepts such as IPv4 addressing, subnet masks, gateways, and routing, and to improve the structure and wording of this README.

The network configurations were completed and verified using the NetPractice training interface.
