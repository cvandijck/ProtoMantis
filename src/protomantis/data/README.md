# Package Data

The data folder will be shipped with protomantis and can therefore contain all necessary data for your 
application. Within the application, the data folder can be referenced by calling the `get_resource_path` function from 
the package `__init__` file.

The content of this data folder can be ignored by git (added to .gitignore) to keep source tracking efficient. The 
application data can be pulled from another data repository, e.g. via git LFS.