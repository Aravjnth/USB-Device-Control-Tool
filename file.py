import tkinter as tk
from tkinter import ttk
import usb.core
import usb.util

class USBDeviceControlTool:
    def __init__(self, root):
        self.root = root
        self.root.title("USB Device Control Tool")
        self.root.geometry("400x300")

        # Create tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)

        # Create frames for each tab
        self.devices_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.devices_frame, text="Devices")

        self.controls_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.controls_frame, text="Controls")

        # Devices tab
        self.devices_label = ttk.Label(self.devices_frame, text="USB Devices:")
        self.devices_label.pack(pady=10)

        self.devices_listbox = tk.Listbox(self.devices_frame, width=40)
        self.devices_listbox.pack(pady=10)

        self.refresh_button = ttk.Button(self.devices_frame, text="Refresh", command=self.refresh_devices)
        self.refresh_button.pack(pady=10)

        # Controls tab
        self.controls_label = ttk.Label(self.controls_frame, text="Device Controls:")
        self.controls_label.pack(pady=10)

        self.device_select_label = ttk.Label(self.controls_frame, text="Select Device:")
        self.device_select_label.pack(pady=5)

        self.device_select_combobox = ttk.Combobox(self.controls_frame, values=[])
        self.device_select_combobox.pack(pady=5)

        self.reset_button = ttk.Button(self.controls_frame, text="Reset Device", command=self.reset_device)
        self.reset_button.pack(pady=10)

        self.disable_button = ttk.Button(self.controls_frame, text="Disable Device", command=self.disable_device)
        self.disable_button.pack(pady=10)

        self.enable_button = ttk.Button(self.controls_frame, text="Enable Device", command=self.enable_device)
        self.enable_button.pack(pady=10)

    def refresh_devices(self):
        self.devices_listbox.delete(0, tk.END)
        devices = usb.core.find(find_all=True)
        for device in devices:
            self.devices_listbox.insert(tk.END, f"Bus {device.bus} Device {device.address}: {device.product}")

    def reset_device(self):
        device = self.device_select_combobox.get()
        if device:
            device = usb.core.find(idVendor=device[0], idProduct=device[1])
            if device:
                device.reset()

    def disable_device(self):
        device = self.device_select_combobox.get()
        if device:
            device = usb.core.find(idVendor=device[0], idProduct=device[1])
            if device:
                device.detach_kernel_driver(0)

    def enable_device(self):
        device = self.device_select_combobox.get()
        if device:
            device = usb.core.find(idVendor=device[0], idProduct=device[1])
            if device:
                device.attach_kernel_driver(0)

if __name__ == "__main__":
    root = tk.Tk()
    tool = USBDeviceControlTool(root)
    root.mainloop()
