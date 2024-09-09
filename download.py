import subprocess
import json


class Downloader:
    def __init__(self, acc_list_file, use = "prefetch", outdir = "./test/raw/") -> None:
        self.acc_list_file = acc_list_file
        self.use = use
        self.outdir = outdir
    
    def _load_config(self):
        with open('config/download.json', 'r') as fd:
            self.config_json = json.load(fd)
    
    def start(self):
        self._load_config()
        cmd = f"{self.config_json[self.use]} -O {self.outdir} --option-file {self.acc_list_file} -p"
        subprocess.check_call(cmd, shell=True)


def main():
    file = "/workspaces/mydev2/list.txt"
    runner = Downloader(file)
    runner.start()

if __name__ == '__main__':
    main()