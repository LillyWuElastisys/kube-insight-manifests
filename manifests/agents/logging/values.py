values = {
    "namespace": "logging",
    "fluentbit": {
        "image": "fluent/fluent-bit",
        "version": "0.13",
        "pullPolicy": "IfNotPresent",
        "cpuRequestMilliCores": 5,
        "memRequestMB": 10,
        "cpuLimitMilliCores": 50,
        "memLimitMB": 60
    },
    "kubeInsightLogServer": {
        "host": "kube-insight-logserver.logging.svc.cluster.local",
        "port": 80
    }
}
