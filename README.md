# VM Luncher Chrome Extension

## Overview

The VM Luncher Chrome Extension allows you to easily manage a virtual machine (VM) on the cloud that has a changing IP address. This extension simplifies the process of launching the VM and connecting to it using Putty.

## Prerequisites

Before using the VM Luncher extension, ensure you have the following installed on your system:

1. **Putty**: Putty is an SSH and Telnet client used to connect to remote servers and VMs. You can download Putty from the official website: [Putty Download](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

2. **Python**: Python is required to run the Native Messaging Host for the extension. Install Python from the official website: [Python Download](https://www.python.org/downloads/)

## Installation

1. Clone the VM Luncher repository to your local machine.
   
3. Load the extension as an unpacked extension in developer mode:

- Open Google Chrome.
- Go to `chrome://extensions/`.
- Enable Developer mode (toggle button usually located at the top-right corner).
- Click on "Load unpacked" and select the `VM_luncher` directory from the cloned repository.

3. After loading the extension, you should see the VM Luncher icon in the Chrome toolbar.

4. Set up the Native Messaging Host:

- Navigate to the `native_messaging` directory.
- Copy the absolute path of the `batexecutor.py` file.
- Open the `manifest.json` file in the `native_messaging` directory and replace `"path/to/batexecutor.py"` with the copied absolute path.

5. Register the Native Messaging Host in the Windows Registry:

- Open the `Command Prompt` as an administrator.
- Navigate to the `native_messaging` directory.
- Run the following command:

  ```
  reg add HKCU\Software\Google\Chrome\NativeMessagingHosts\com.example.batexecutor /ve /t REG_SZ /d "<absolute_path_to_native_messaging_directory>\manifest.json"
  ```

Replace `<absolute_path_to_native_messaging_directory>` with the absolute path of the `native_messaging` directory.

6. You have successfully installed VM Luncher Chrome Extension! Click on the extension icon in the Chrome toolbar to open the popup and start using it.

**Note**: Be cautious when modifying the Windows Registry. Incorrect changes can cause system issues. Always make sure to create a backup before making any modifications.


## Usage

Follow the steps below to use the VM Luncher Chrome Extension:

1. **Copy IP Address**: Copy the IP address of the VM to your clipboard. This can usually be found in your VM provider's dashboard.

2. **Paste IP Address**: Click on the VM Luncher extension icon in the Chrome toolbar to open the popup. Paste the IP address in the input field.

3. **Launch VM**: Click on the "Lunch VM" button to initiate the connection to the VM. The extension will execute a batch file using the IP address you provided. The batch file will open Putty and connect to the VM.

4. **Access Your VM**: Putty will open, and you should see a terminal window connected to your VM. Enter your login credentials when prompted to access your VM.

## Native Messaging Host

The extension uses a Native Messaging Host to communicate with a Python script that executes the batch file with the IP address. The Python script receives messages from the extension, processes them, and sends back responses.

Note: Native Messaging Host is Native Messaging Hosting allows Chrome extensions to communicate with external native applications on a user's computer, enabling advanced functionalities beyond regular web technologies. It bridges the gap between extensions and native code, enabling more powerful tasks while maintaining security.

## Registry Configuration

The extension requires a registry configuration to run the Native Messaging Host. Please make sure you have set up the registry correctly as explained in the extension's documentation.
```diff
- Modifying the registry settings incorrectly can cause system instability or other unexpected issues.
```

## Troubleshooting

If you encounter any issues with the extension, ensure that you have installed the prerequisites (Putty and Python) and have configured the registry correctly. You can also check the browser console and the Python script's output for any error messages.

## License

This project is licensed under the [MIT License](LICENSE).
