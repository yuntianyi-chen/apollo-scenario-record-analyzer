# Apollo Scenario Record Violation Analyzer
Scenario Violation Analyzer for Apollo CyberRecord Records

### Directory Structure
```
|--PROJECT_ROOT
   |--data
      |--maps
      |--records
   |--src
      |--environment
      |--modules
      |--objectives
      |--tools
      |--config.py
      |--run_analyzer.py
  ```

## Supporting Violation Types
| Violation Type           | Non-strict Features                                                     | Strict Features |
|--------------------------|-------------------------------------------------------------------------|-----------------|
| Collision               | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$,$p^{O}_{t}$,$s^{O}_{t}$,$h^{O}_{t}$ | -               |
| Fast Acceleration       | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$,$duration$,$accel$                  | -               |
| Hard Braking           | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$,$duration$,$decel$                  | -               |
| Speeding               | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$,$duration$                          | -               |
| Unsafe Lane-change     | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$,$duration$                          | -               |
| Lane-change in Junction | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$                                     | $id_{junction}$ |
| Module Delay           | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$,$duration$                          | $type_{module}$ |
| Module Malfunction     | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$                                     | $type_{module}$ |
| Vehicle Paralysis      | $p^{E}_{t}$,$s^{E}_{t}$,$h^{E}_{t}$                                     | $type_{module}$ |


### Prepare Steps

1. Place your maps under the `data/maps` directory.

2. (Optional) Create a python virtual environment using `python3 create -m venv ./venv && source ./venv/bin/activate`

3. Install dependencies using `poetry install`.


## Usage
- Configure the `map_name` and `scenario_record_path` in the `run_analyzer.py` file.

- Run outside the docker container:
```bash
python3 src/run_analyzer.py
```


## Paper Citation
```aiignore
@article{ChenHLHG24,
  author       = {Yuntianyi Chen and
                  Yuqi Huai and
                  Shilong Li and
                  Changnam Hong and
                  Joshua Garcia},
  title        = {Misconfiguration Software Testing for Failure Emergence in Autonomous
                  Driving Systems},
  journal      = {Proc. {ACM} Softw. Eng.},
  volume       = {1},
  number       = {{FSE}},
  pages        = {1913--1936},
  year         = {2024},
  url          = {https://doi.org/10.1145/3660792},
  doi          = {10.1145/3660792},
  timestamp    = {Fri, 02 Aug 2024 21:41:21 +0200},
  biburl       = {https://dblp.org/rec/journals/pacmse/ChenHLHG24.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```