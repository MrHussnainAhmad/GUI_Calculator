# GUI_Calculator
Description:

This Python script creates a graphical user interface (GUI) calculator using the tkinter library. The calculator allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and modulus, with an option to choose between integer and float modes. The window size of the calculator is fixed to ensure a consistent user experience.
Features:

    Mode Selection:
        Users can switch between integer and float modes by clicking the respective buttons (Integer and Float). The current mode is displayed at the top of the calculator.
        In integer mode, the results of calculations are converted to integers.
        In float mode, the results are displayed as floating-point numbers.

    Basic Arithmetic Operations:
        The calculator supports addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).
        Buttons for digits (0-9), decimal point (.), and arithmetic operations are provided.

    Additional Functionality:
        C button: Clears the current input.
        ← button: Deletes the last character in the current input.
        = button: Evaluates the expression entered by the user.

    User Interface:
        An entry widget at the top of the window displays the current input and results.
        The buttons are arranged in a grid layout for easy access and usability.
        The window is centered on the screen when opened, with a fixed width of 400 pixels and a height of 500 pixels. The window size cannot be changed by the user, ensuring a consistent appearance.

Detailed Code Explanation:

    Imports:
        The script imports the tkinter library, which is used for creating the GUI.

    Mode Setting Function:
        set_mode(mode): This function sets the global conversion_mode to either 'i' (integer) or 'f' (float) and updates the mode label displayed on the calculator.

    Button Press Function:
        press(key): This function updates the entry widget with the key pressed by the user.

    Evaluate Function:
        evaluate(): This function evaluates the arithmetic expression entered by the user. It handles errors and ensures that the result is displayed according to the selected mode (integer or float).

    Clear and Backspace Functions:
        clear(): Clears the entry widget.
        backspace(): Deletes the last character in the entry widget.

    Window Centering Function:
        center_window(root, width, height): This function centers the window on the screen based on the given width and height.

    Main Program:
        The main part of the script initializes the tkinter root window, sets up the entry widget and mode label, and creates buttons for digits, operations, and additional functionalities.
        The center_window function is called to center the window, and root.resizable(False, False) is used to disable window resizing.
        The root.mainloop() function starts the GUI event loop, allowing the user to interact with the calculator.

By running this script, users can interact with a functional and user-friendly calculator with a fixed-size window that supports both integer and float calculations.
