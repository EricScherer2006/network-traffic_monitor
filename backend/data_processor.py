def aggregate_stats(packet_info):
    protocol = packet_info.get("protocol", "Unknown")
    size = packet_info.get("size", 0)
    # Aggregate data for visualization
    return {"protocol": protocol, "size": size}