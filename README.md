# create png diagrams using graphvis and diagrams

https://medium.com/@arnab.sen44/create-neat-technical-diagrams-using-python-4e5296b78c02

## Setup:
* brew install graphviz  
* pip install diagrams  

## Simple format

grouped_workers.py

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=False, direction="TB"):
    ELB("lb") >> [EC2("worker1"),
                EC2("worker2"),
                EC2("worker3"),
                EC2("worker4"),
                EC2("worker5")] >> RDS("events")
```

grouped_workers.png

<img src="grouped_workers.png" alt="diagram" style="width:400px;"/>
