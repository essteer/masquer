# Local development

The following details will assist with making and testing changes to a cloned version of the repository.

## Updates

The root directory includes a shell script `update.sh` for convenience to update JSON assets for the `masquer` package.

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)

```console
$ chmod +x update.sh
$ ./update.sh
Update successful
```

If using your own JSON data you can still make use of the `update_assets()` function inside `update.py` to sync changes with the `assets.py` file inside the `masquer` package.

## Tests

`masquer` uses Python's in-built `unittest` module. 

To run the entire test suite using `discover`, or specify an individual test file from the `tests` directory — for example `test_assets.py` — run one of the following shell commands from the project `root` directory:

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)
![](https://img.shields.io/badge/macOS-000000.svg?style=flat&logo=Apple&logoColor=white)

```console
$ python3 -m unittest discover  # run all tests
$ python3 -m unittest tests.test_assets  # test a single file
```

![](https://img.shields.io/badge/Windows-0078D4.svg?style=flat&logo=Windows&logoColor=white)

```console
$ python -m unittest discover  # run all tests
$ python -m unittest tests.test_assets  # test a single file
```
