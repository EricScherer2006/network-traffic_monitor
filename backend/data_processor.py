def aggregate_stats(packet_info):
    protocol = packet_info.get("protocol", "Unknown")
    size = packet_info.get("size", 0)
    src = packet_info.get("src", "Unknown")
    dst = packet_info.get("dst", "Unknown")
    # Aggregate data for visualization
    return {
        "protocol": protocol,
        "size": size,
        "src": src,
        "dst": dst
    }