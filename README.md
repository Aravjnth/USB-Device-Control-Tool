 USB Device Control Tool

## Overview

The USB Device Control Tool is a Python-based application designed to manage and monitor USB devices connected to a computer. This tool provides functionalities to enable or disable USB ports, monitor USB device activity, and generate reports on USB device usage, making it useful for security and administrative purposes.

## Features

- Enable or disable USB ports.
- Monitor USB device connections and disconnections.
- Log detailed information about connected USB devices.
- Generate reports on USB device activity.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- `pyusb` library

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/USB-Device-Control-Tool.git
    cd usb-device-control-tool
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool to enable or disable USB ports:
    ```bash
    python usb_control.py --action <enable|disable> --port <port-number>
    ```

2. Run the tool to monitor USB device activity:
    ```bash
    python usb_control.py --action monitor
    ```

3. Generate a report on USB device activity:
    ```bash
    python usb_control.py --action report --output <output-file>
    ```

    Replace `<enable|disable>`, `<port-number>`, and `<output-file>` with the actual values.

### Example

Enable USB port 1:

```bash
python usb_control.py --action enable --port 1
```

Monitor USB device activity:

```bash
python usb_control.py --action monitor
```

Generate a report on USB device activity and save it to `usb_activity_report.txt`:

```bash
python usb_control.py --action report --output usb_activity_report.txt
```

## Options

- `--action`: Action to perform (enable, disable, monitor, report).
- `--port`: USB port number to enable or disable (required for enable/disable action).
- `--output`: Path to the output file for the report (required for report action).

## Legal Disclaimer

This tool is intended for educational purposes and ethical use only. Unauthorized use of this tool to control or monitor USB devices without proper authorization is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj
