import LoggerPack.log_container as lc
import docker
from docker import errors
import sys

if __name__ == "__main__":
    lc.logger.error("This file cannot be run as main!")
    print("\nThis file cannot be run as main!")
    sys.exit()

try:
    client = docker.from_env()
except errors.DockerException:
    lc.logger.error("Docker is not working right now!")

def get_container_metrics():

    containers = client.containers.list()
    containers_stats = []
    for container in containers:
        stats = container.stats(stream=False)

        cpu_percent = calculate_cpu_percent(stats)
        image = container.image.tags[0] if container.image.tags else "N/A"
        created = container.attrs['Created']
        # ports = container.attrs['NetworkSettings']['Ports']
        mem_usage_mb = stats["memory_stats"]["usage"] / (1024 * 1024)
        containers_stats.append(f"~  Container name: {container.name} \n"
                                f"~  Container status: {container.status} \n"
                                f"~  Parent image: {image} \n"
                                f"~  Time created: {created} \n"
                                f"~  CPU load: {cpu_percent:.2f} % \n"
                                f"~  RAM use: {mem_usage_mb:.2f} MB\n")
    return containers_stats

def calculate_cpu_percent(stats):
    cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - stats["precpu_stats"]["cpu_usage"]["total_usage"]
    system_delta = stats["cpu_stats"]["system_cpu_usage"] - stats["precpu_stats"]["system_cpu_usage"]

    if system_delta > 0:
        return (cpu_delta / system_delta) * len(stats["cpu_stats"]["cpu_usage"]["percpu_usage"]) * 100.0
    return 0.0

def get_container_status_real_time():
    containers = client.containers.list()
    for container in containers:
        stats = container.stats(stream=False)
        cpu_percent = calculate_cpu_percent(stats)

        if float(cpu_percent) > 50.00:
            return f"The container {container.name} uses more than 50% of the available processor resources on the host"

        mem_usage_mb = stats["memory_stats"]["usage"] / (1024 * 1024)
        if float(mem_usage_mb) > 500.00:
            return f"The container {container.name} uses 500 MB of the available RAM resources on the host"

        return 0





