# LLVM Lookup Tool
This command-line tool returns the LLVM Static Complier arguments based on a common board name such as "Arduino Uno".

## More info
ELL offers a path for ML model to be complied for microcontrollers and single chip computers. One limitation of ELL is that very few devices are offered as built in targets, since ELL uses LLVM to compile the models just about any chip available can be targeted. However, LLVM is a tool designed for a highly technical audience and finding the attributes needed for the complier can be challenging and time consuming. This tool is designed to make it easier to use ELL for common MCUs.

Before using this tool, we recommend that you have some familiarity with ELL, python, and command line interfaces.

### What is LLVM?
LLVM is a set of compiler and toolchain technologies. It's contains multiple components - front ends, intermediate representations, and back ends that span compilation. The LLVM IR Optimizer takes the source and using the single optimizer can target a range of hardware, defined by the arguments.
More information can be found at the [LLVM Github page](https://github.com/llvm/llvm-project).

## How to use the lookup tool
Run the tool using python:
python get_llvm.py


# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
