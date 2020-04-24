# LLVM Lookup Tool
This command-line tool returns the LLVM Static Compiler arguments based on a common microcontroller, or MCU, board name such as "Arduino Uno".

## More info
ELL offers a path for ML model to be complied for microcontrollers and single chip computers. One limitation of ELL is that very few devices are offered as built in targets, since ELL uses LLVM to compile the models just about any chip available can be targeted. However, LLVM is a tool designed for a highly technical audience and finding the attributes needed for the complier can be challenging and time consuming. This tool is designed to make it easier to use ELL for common MCUs.

The core of this project is a JSON database. This includes the common name for the board, a device id, and LLVM arguments needed for compiling.

Before using this tool, we recommend that you have some familiarity with ELL, python, and command line interfaces.

### What is LLVM?
LLVM is a set of compiler and toolchain technologies. It's contains multiple components - front ends, intermediate representations, and back ends that span compilation. The LLVM IR Optimizer takes the source and using the single optimizer can target a range of hardware, defined by the arguments.
More information can be found at the [LLVM Github page](https://github.com/llvm/llvm-project).

## How to use the lookup tool
Run the tool in terminal using python:
`python get_llvm.py`

Get the LLVM triple and other attributes:
`python get_llvm.py --get "Board Name"`

Search for an available board:
`python get_llvm.py --search "Board"`

List all available boards:
`python get_llvm.py --list`

Copy the LLVM arguments and save to input during compiling. Note that boards may have different numbers of attributes.

**Please note that the LLVM lookup program is currently case sensitive.** 
If you do not see the board you are looking for, check capitalization and spelling.

# Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Adding boards
Please help us add boards! 
To add your own or other favorite boards, fork this repo and make the relevant edits to the boards.json file, then submit a pull request indicating what boards you have added.
## Where to find LLVM Arguments
Finding the LLVM triple and other attributes will depend on the hardware and firmware of your particular device. The LLVM triple is a string that includes the architecture of the MCU and the type of compiling (e.g. bare metal, GNU).

Here are some places to look:
* Manufacturer datasheets
* If you're using GNU with Arm [here is a helpful guide](https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html)