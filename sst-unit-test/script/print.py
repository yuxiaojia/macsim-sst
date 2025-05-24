for core_id in range(0, 16):
    print(f"""
########################################
# Core {core_id}

# Interfaces
macsim_icache_if_{core_id} = macsim.setSubComponent("core{core_id}_icache", "memHierarchy.standardInterface")
macsim_icache_if_{core_id}.addParams({{
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
}})
macsim_dcache_if_{core_id} = macsim.setSubComponent("core{core_id}_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_{core_id}.addParams({{
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
}})
macsim_ccache_if_{core_id} = macsim.setSubComponent("core{core_id}_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_{core_id}.addParams({{
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
}})
macsim_tcache_if_{core_id} = macsim.setSubComponent("core{core_id}_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_{core_id}.addParams({{
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
}})

########################################
# L1 Caches
core{core_id}_icache = sst.Component("core{core_id}_icache", "memHierarchy.Cache")
core{core_id}_icache.addParams({{
    "access_latency_cycles": "3",
    "cache_frequency": "3.5Ghz",
    "replacement_policy": "lru",
    "coherence_protocol": "MSI",
    "associativity": "4",
    "cache_line_size": "64",
    "debug": DEBUG_L1,
    "debug_level": DEBUG_LEVEL,
    "verbose": VERBOSE,
    "L1": "1",
    "cache_size": "2KiB"
}})

core{core_id}_dcache = sst.Component("core{core_id}_dcache", "memHierarchy.Cache")
core{core_id}_dcache.addParams({{
    "access_latency_cycles": "3",
    "cache_frequency": "3.5Ghz",
    "replacement_policy": "lru",
    "coherence_protocol": "MSI",
    "associativity": "4",
    "cache_line_size": "64",
    "debug": DEBUG_L1,
    "debug_level": DEBUG_LEVEL,
    "verbose": VERBOSE,
    "L1": "1",
    "cache_size": "2KiB"
}})

core{core_id}_ccache = sst.Component("core{core_id}_ccache", "memHierarchy.Cache")
core{core_id}_ccache.addParams({{
    "access_latency_cycles": "3",
    "cache_frequency": "3.5Ghz",
    "replacement_policy": "lru",
    "coherence_protocol": "MSI",
    "associativity": "4",
    "cache_line_size": "128",
    "debug": DEBUG_L1,
    "debug_level": DEBUG_LEVEL,
    "verbose": VERBOSE,
    "L1": "1",
    "cache_size": "2KiB"
}})

core{core_id}_tcache = sst.Component("core{core_id}_tcache", "memHierarchy.Cache")
core{core_id}_tcache.addParams({{
    "access_latency_cycles": "3",
    "cache_frequency": "3.5Ghz",
    "replacement_policy": "lru",
    "coherence_protocol": "MSI",
    "associativity": "4",
    "cache_line_size": "128",
    "debug": DEBUG_L1,
    "debug_level": DEBUG_LEVEL,
    "verbose": VERBOSE,
    "L1": "1",
    "cache_size": "2KiB"
}})
""")


print("""
########################################
# Bus between L1 caches and memory controller
mem_bus = sst.Component("mem_bus", "memHierarchy.Bus")
mem_bus.addParams({
    "debug" : DEBUG_LINKS,
    "debug_level" : DEBUG_LEVEL,
    "bus_frequency" : "4 Ghz"
})


########################################
# Memory Controller
memctrl = sst.Component("memctrl", "memHierarchy.MemController")
memctrl.addParams({
    "debug" : DEBUG_MEM,
    "debug_level" : DEBUG_LEVEL,
    "clock" : "1GHz",
    "verbose" : VERBOSE,
    # "addr_range_start" : MEM_START,
    "addr_range_end" : MEM_END,
})
memory = memctrl.setSubComponent("backend", "memHierarchy.simpleMem")
memory.addParams({
    "access_time" : "1000ns",
    "mem_size" : MEM_SIZE_S
})
""")


for core_id in range(0, 16):
    print(f"""
# Links for Core {core_id}
link_macsim_icache_{core_id} = sst.Link("link_macsim_icache_{core_id}")
link_macsim_icache_{core_id}.connect((macsim_icache_if_{core_id}, "port", "1000ps"), (core{core_id}_icache, "high_network_0", "1000ps"))

link_macsim_dcache_{core_id} = sst.Link("link_macsim_dcache_{core_id}")
link_macsim_dcache_{core_id}.connect((macsim_dcache_if_{core_id}, "port", "1000ps"), (core{core_id}_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_{core_id} = sst.Link("link_macsim_ccache_{core_id}")
link_macsim_ccache_{core_id}.connect((macsim_ccache_if_{core_id}, "port", "1000ps"), (core{core_id}_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_{core_id} = sst.Link("link_macsim_tcache_{core_id}")
link_macsim_tcache_{core_id}.connect((macsim_tcache_if_{core_id}, "port", "1000ps"), (core{core_id}_tcache, "high_network_0", "1000ps"))
""")

port_index = 0
for core_id in range(0, 16):
    print(f"""
# Links bus for Core {core_id}
link_icache_bus_{core_id} = sst.Link("link_icache_bus_{core_id}")
link_icache_bus_{core_id}.connect((core{core_id}_icache, "low_network_0", "50ps"), (mem_bus, "high_network_{port_index}", "50ps"))

link_dcache_bus_{core_id} = sst.Link("link_dcache_bus_{core_id}")
link_dcache_bus_{core_id}.connect((core{core_id}_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_{port_index + 1}", "50ps"))

link_ccache_bus_{core_id} = sst.Link("link_ccache_bus_{core_id}")
link_ccache_bus_{core_id}.connect((core{core_id}_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_{port_index + 2}", "50ps"))

link_tcache_bus_{core_id} = sst.Link("link_tcache_bus_{core_id}")
link_tcache_bus_{core_id}.connect((core{core_id}_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_{port_index + 3}", "50ps"))
""")
    port_index += 4



print('''# Bus -> Memory
link_bus_mem = sst.Link("link_bus_mem")
link_bus_mem.connect( (mem_bus, "low_network_0", "50ps"), (memctrl, "direct_link", "50ps") )


########################################
# Enable statistics
sst.setStatisticLoadLevel(7)
sst.setStatisticOutput("sst.statOutputConsole")''')
