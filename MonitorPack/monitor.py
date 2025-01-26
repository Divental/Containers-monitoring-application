import docker

client = docker.from_env()

def get_container_metrics():

    containers = client.containers.list()
    containers_stats = []
    for container in containers:
        stats = container.stats(stream=False)

        cpu_percent = calculate_cpu_percent(stats)
        mem_usage_mb = stats["memory_stats"]["usage"] / (1024 * 1024)  # Перетворення в МБ
        containers_stats.append(f"Container: {container.name} | CPU: {cpu_percent:.2f}% | RAM: {mem_usage_mb:.2f} MB\n")
    return containers_stats

def calculate_cpu_percent(stats):
    cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - stats["precpu_stats"]["cpu_usage"]["total_usage"]
    system_delta = stats["cpu_stats"]["system_cpu_usage"] - stats["precpu_stats"]["system_cpu_usage"]

    if system_delta > 0:
        return (cpu_delta / system_delta) * len(stats["cpu_stats"]["cpu_usage"]["percpu_usage"]) * 100.0
    return 0.0





