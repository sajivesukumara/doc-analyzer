#!/usr/bin/env python3
import json
import sys

def get_router_details():
    # Your logic here
    result = ('available', 'slugger_standalone-sj21-fff-34-03', 'slugger', 
              'standalone', 'Slugger', 'slugger_standalone')
    print(json.dumps(list(result)))  # Convert tuple to list for JSON
    return 0


def main():
    # Return a list
    routers = [
        {"router_id": 123, "router_name": "churchill-01", "status": "available"},
        {"router_id": 124, "router_name": "churchill-02", "status": "busy"},
        {"router_id": 125, "router_name": "slugger-01", "status": "available"}
    ]

    output = ('first','second','third','fourth','fifth')
    
    print(json.dumps(routers))
    return 0

if __name__ == "__main__":
    sys.exit(get_router_details())
    sys.exit(main())


