# Teleporte Compose Documentation

> [!NOTE]  
> 🇫🇷 [Documentation disponible en français](README_fr.md)

Welcome to the **Teleporte Compose** documentation. Here you'll find all the information you need to understand, install, and use this project.

> [!IMPORTANT]  
> Our documentation is a work in progress. Please be patient or feel free to [contribute](#contribute).

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Using DevContainers with VSCode](#using-devcontainers-with-vscode)
     - [Attaching VSCode to a Running Container](#attaching-vscode-to-a-running-container)
       - [How-to Video: Attach to a Running Container](#how-to-video-attach-to-a-running-container)
     - [Using a DevContainer Defined in a Git Repository](#using-a-devcontainer-defined-in-a-git-repository)
       - [How-to Video: Using a DevContainer Configuration](#how-to-video-using-a-devcontainer-configuration)
     - [What are DevContainers?](#what-are-devcontainers)
4. [Contribute](#contribute)
5. [License](#license)

## Introduction

This project aims to offer an [Internal Developer Platform](https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/) for educational purposes, but it can also be adapted for other uses.

## Installation

To install this project, please refer to the root [README](../README.md).

## Usage

### Using DevContainers with VSCode

To use DevContainers with VSCode, you first need to install the "[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)" extension or the "[Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)". These extensions allow you to work with containers, virtual machines, or remote environments directly from VSCode.

* Here are two common use cases for DevContainers with VSCode:
  1. **Attaching VSCode to a running container**
  2. **Using a DevContainer defined in a Git repository**

> [!TIP] 
> DevContainers combined with VSCode offer a powerful way to standardize development environments within a team, while retaining the benefits of working with a full local IDE.
> Feel free to explore the different DevContainer configuration options to adapt them to your specific needs. The official VSCode documentation is an excellent resource to go further.

#### Attaching VSCode to a Running Container

* To attach a DevContainer to a running container, follow these steps:
  1. Make sure you have the "Dev Containers" extension or the "Remote Development Extension Pack" installed in your VS Code.
  2. Open the Command Palette in VS Code (Ctrl+Shift+P or Cmd+Shift+P on macOS).
  3. Type "Remote-Containers: Attach to Running Container" and select it from the list.
  4. VS Code will display a list of running containers. Choose the container you want to attach to.
  5. After selecting the container, VS Code will reload and attach itself to the running container.
  6. You can now interact with the container through the VS Code interface, edit files, run commands, and debug your application as if it were running locally.

> [!TIP]
> By attaching a DevContainer to a running container, you can leverage the isolated environment and specific dependencies of the container while still using your preferred IDE. This approach is particularly useful when working with existing containers or when you need to quickly debug an issue in a containerized environment.

##### How-to Video: Attach to a Running Container

You can easily attach VSCode to a Docker container already running on your machine. This allows you to develop within the isolated environment of the container.

* To see how to do this in detail, watch this video:
  https://github.com/O-clock-Dev/teleporter-compose/assets/126659374/71df8064-6cfa-414d-8e4d-ceac2b90fed3

#### Using a DevContainer Defined in a Git Repository

If you have a project directory that includes a `devcontainer.json` file, you can easily open it in a DevContainer using VS Code. The `devcontainer.json` file defines the configuration for the development environment, including the base image, VS Code settings, extensions, and more. To open the directory in a DevContainer, follow these steps:

1. Ensure that you have the "Dev Containers" extension or the "Remote Development Extension Pack" installed in your VS Code.
2. Open the project directory in VS Code either by using the "File > Open Folder" menu or by running the `code /path/to/your/project` command in your terminal.
3. Once the directory is opened in VS Code, you should see a notification in the lower right corner indicating that a DevContainer configuration file has been detected.
4. Click on the "Reopen in Container" button in the notification or open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on macOS) and select "Remote-Containers: Reopen in Container".
5. VS Code will build the DevContainer based on the configuration in the `devcontainer.json` file and reopen the directory inside the container.
6. After the build process is complete, you can start developing within the DevContainer environment. Any extensions specified in the configuration will be automatically installed, and the settings will be applied.

> [!TIP]
> By using a `devcontainer.json` file, you can ensure that everyone working on the project has the same development environment, regardless of their local setup. This approach helps to minimize environment-related issues and makes it easier for new team members to start contributing to the project quickly.

##### How-to Video: Using a DevContainer Configuration

Many projects include a DevContainer configuration directly in their Git repository (as in the example in the `code/node/test-app/` folder). This allows all developers to work in a standardized environment.

* To learn how to use such a configuration, follow the tutorial in this video:
  https://github.com/O-clock-Dev/teleporter-compose/assets/126659374/3741a5b7-878c-4b90-888e-8dfd4b42342e

#### What are DevContainers?

The [DevContainers specification](https://containers.dev/) is an open standard that allows you to consistently define and share development environments across different tools and platforms. By leveraging this specification, you can ensure that all developers within a project have access to the same setup, regardless of their local environment. The specification supports a wide range of features, such as specifying the base image, configuring VS Code settings, installing extensions, and more. Adopting the DevContainers specification can greatly simplify the onboarding process for new team members and reduce the time spent on environment-related issues.

## Contribute

Contributions are welcome! Please read the [contribution guidelines](../CONTRIBUTING.md) for more details.

## License

This project is licensed under the AGPLv3 license. See the [LICENSE](../LICENSE) file for details.