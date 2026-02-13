import os

def find_node():
    drives = ["C:\\"]
    paths = [
        r"Program Files\nodejs",
        r"Program Files (x86)\nodejs",
        r"Users\DELL\AppData\Roaming\npm",
        r"Users\DELL\AppData\Local\nvs",
        r"Users\DELL\.nvm"
    ]
    
    for drive in drives:
        for path in paths:
            full_path = os.path.join(drive, path)
            node_exe = os.path.join(full_path, "node.exe")
            npm_cmd = os.path.join(full_path, "npm.cmd")
            
            if os.path.exists(node_exe):
                print(f"Node found: {node_exe}")
                if os.path.exists(npm_cmd):
                    print(f"NPM found: {npm_cmd}")
                return
    
    print("Node not found in common locations.")

if __name__ == "__main__":
    find_node()
