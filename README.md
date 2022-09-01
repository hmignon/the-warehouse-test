# The-Warehouse-Test

**Technical test for OSS Factory:** Find the 2 IDs within the list with one differing 
character at the same index ([more details](https://mergify.notion.site/The-Warehouse-158c1275890e4157a77112609fd7a129) about the problem).

*Windows 10 - Python 3.9.5*

## Usage

*No third-party packages are needed for both scripts.*

Download or clone the repository: ```git clone https://github.com/hmignon/the-warehouse-test.git```

Run the checksum: ```python checksum.py```

Find correct boxes: ```python find_boxes.py```


## Results

- **Checksum value:** `9633`


- **Correct box IDs:** `lujnogabetpumsydyfcovzixaw` and `lujnogabetprmsydyfcovzixaw` 

- **Common letters:** `lujnogabetpmsydyfcovzixaw`

- **Diff:** `u`u and `r` at index `11`

## Improvements and limits


- Select other files with command-line arguments
  - Run a check before importing to validate file type and data (no empty files, IDs with same length, etc)
- Run *checksum* before import, raise exception if value is incorrect
- Larger quantities of data will proportionally increase runtime of the scripts
  - Consider using a more optimised solution for very large datasets
