
########################################
# Core 0

# Interfaces
macsim_icache_if_0 = macsim.setSubComponent("core0_icache", "memHierarchy.standardInterface")
macsim_icache_if_0.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_0 = macsim.setSubComponent("core0_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_0.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_0 = macsim.setSubComponent("core0_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_0.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_0 = macsim.setSubComponent("core0_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_0.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core0_icache = sst.Component("core0_icache", "memHierarchy.Cache")
core0_icache.addParams({
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
})

core0_dcache = sst.Component("core0_dcache", "memHierarchy.Cache")
core0_dcache.addParams({
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
})

core0_ccache = sst.Component("core0_ccache", "memHierarchy.Cache")
core0_ccache.addParams({
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
})

core0_tcache = sst.Component("core0_tcache", "memHierarchy.Cache")
core0_tcache.addParams({
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
})


########################################
# Core 1

# Interfaces
macsim_icache_if_1 = macsim.setSubComponent("core1_icache", "memHierarchy.standardInterface")
macsim_icache_if_1.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_1 = macsim.setSubComponent("core1_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_1.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_1 = macsim.setSubComponent("core1_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_1.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_1 = macsim.setSubComponent("core1_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_1.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core1_icache = sst.Component("core1_icache", "memHierarchy.Cache")
core1_icache.addParams({
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
})

core1_dcache = sst.Component("core1_dcache", "memHierarchy.Cache")
core1_dcache.addParams({
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
})

core1_ccache = sst.Component("core1_ccache", "memHierarchy.Cache")
core1_ccache.addParams({
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
})

core1_tcache = sst.Component("core1_tcache", "memHierarchy.Cache")
core1_tcache.addParams({
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
})


########################################
# Core 2

# Interfaces
macsim_icache_if_2 = macsim.setSubComponent("core2_icache", "memHierarchy.standardInterface")
macsim_icache_if_2.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_2 = macsim.setSubComponent("core2_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_2.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_2 = macsim.setSubComponent("core2_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_2.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_2 = macsim.setSubComponent("core2_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_2.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core2_icache = sst.Component("core2_icache", "memHierarchy.Cache")
core2_icache.addParams({
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
})

core2_dcache = sst.Component("core2_dcache", "memHierarchy.Cache")
core2_dcache.addParams({
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
})

core2_ccache = sst.Component("core2_ccache", "memHierarchy.Cache")
core2_ccache.addParams({
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
})

core2_tcache = sst.Component("core2_tcache", "memHierarchy.Cache")
core2_tcache.addParams({
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
})


########################################
# Core 3

# Interfaces
macsim_icache_if_3 = macsim.setSubComponent("core3_icache", "memHierarchy.standardInterface")
macsim_icache_if_3.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_3 = macsim.setSubComponent("core3_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_3.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_3 = macsim.setSubComponent("core3_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_3.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_3 = macsim.setSubComponent("core3_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_3.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core3_icache = sst.Component("core3_icache", "memHierarchy.Cache")
core3_icache.addParams({
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
})

core3_dcache = sst.Component("core3_dcache", "memHierarchy.Cache")
core3_dcache.addParams({
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
})

core3_ccache = sst.Component("core3_ccache", "memHierarchy.Cache")
core3_ccache.addParams({
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
})

core3_tcache = sst.Component("core3_tcache", "memHierarchy.Cache")
core3_tcache.addParams({
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
})


########################################
# Core 4

# Interfaces
macsim_icache_if_4 = macsim.setSubComponent("core4_icache", "memHierarchy.standardInterface")
macsim_icache_if_4.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_4 = macsim.setSubComponent("core4_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_4.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_4 = macsim.setSubComponent("core4_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_4.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_4 = macsim.setSubComponent("core4_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_4.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core4_icache = sst.Component("core4_icache", "memHierarchy.Cache")
core4_icache.addParams({
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
})

core4_dcache = sst.Component("core4_dcache", "memHierarchy.Cache")
core4_dcache.addParams({
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
})

core4_ccache = sst.Component("core4_ccache", "memHierarchy.Cache")
core4_ccache.addParams({
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
})

core4_tcache = sst.Component("core4_tcache", "memHierarchy.Cache")
core4_tcache.addParams({
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
})


########################################
# Core 5

# Interfaces
macsim_icache_if_5 = macsim.setSubComponent("core5_icache", "memHierarchy.standardInterface")
macsim_icache_if_5.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_5 = macsim.setSubComponent("core5_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_5.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_5 = macsim.setSubComponent("core5_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_5.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_5 = macsim.setSubComponent("core5_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_5.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core5_icache = sst.Component("core5_icache", "memHierarchy.Cache")
core5_icache.addParams({
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
})

core5_dcache = sst.Component("core5_dcache", "memHierarchy.Cache")
core5_dcache.addParams({
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
})

core5_ccache = sst.Component("core5_ccache", "memHierarchy.Cache")
core5_ccache.addParams({
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
})

core5_tcache = sst.Component("core5_tcache", "memHierarchy.Cache")
core5_tcache.addParams({
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
})


########################################
# Core 6

# Interfaces
macsim_icache_if_6 = macsim.setSubComponent("core6_icache", "memHierarchy.standardInterface")
macsim_icache_if_6.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_6 = macsim.setSubComponent("core6_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_6.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_6 = macsim.setSubComponent("core6_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_6.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_6 = macsim.setSubComponent("core6_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_6.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core6_icache = sst.Component("core6_icache", "memHierarchy.Cache")
core6_icache.addParams({
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
})

core6_dcache = sst.Component("core6_dcache", "memHierarchy.Cache")
core6_dcache.addParams({
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
})

core6_ccache = sst.Component("core6_ccache", "memHierarchy.Cache")
core6_ccache.addParams({
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
})

core6_tcache = sst.Component("core6_tcache", "memHierarchy.Cache")
core6_tcache.addParams({
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
})


########################################
# Core 7

# Interfaces
macsim_icache_if_7 = macsim.setSubComponent("core7_icache", "memHierarchy.standardInterface")
macsim_icache_if_7.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_7 = macsim.setSubComponent("core7_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_7.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_7 = macsim.setSubComponent("core7_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_7.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_7 = macsim.setSubComponent("core7_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_7.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core7_icache = sst.Component("core7_icache", "memHierarchy.Cache")
core7_icache.addParams({
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
})

core7_dcache = sst.Component("core7_dcache", "memHierarchy.Cache")
core7_dcache.addParams({
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
})

core7_ccache = sst.Component("core7_ccache", "memHierarchy.Cache")
core7_ccache.addParams({
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
})

core7_tcache = sst.Component("core7_tcache", "memHierarchy.Cache")
core7_tcache.addParams({
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
})


########################################
# Core 8

# Interfaces
macsim_icache_if_8 = macsim.setSubComponent("core8_icache", "memHierarchy.standardInterface")
macsim_icache_if_8.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_8 = macsim.setSubComponent("core8_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_8.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_8 = macsim.setSubComponent("core8_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_8.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_8 = macsim.setSubComponent("core8_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_8.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core8_icache = sst.Component("core8_icache", "memHierarchy.Cache")
core8_icache.addParams({
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
})

core8_dcache = sst.Component("core8_dcache", "memHierarchy.Cache")
core8_dcache.addParams({
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
})

core8_ccache = sst.Component("core8_ccache", "memHierarchy.Cache")
core8_ccache.addParams({
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
})

core8_tcache = sst.Component("core8_tcache", "memHierarchy.Cache")
core8_tcache.addParams({
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
})


########################################
# Core 9

# Interfaces
macsim_icache_if_9 = macsim.setSubComponent("core9_icache", "memHierarchy.standardInterface")
macsim_icache_if_9.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_9 = macsim.setSubComponent("core9_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_9.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_9 = macsim.setSubComponent("core9_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_9.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_9 = macsim.setSubComponent("core9_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_9.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core9_icache = sst.Component("core9_icache", "memHierarchy.Cache")
core9_icache.addParams({
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
})

core9_dcache = sst.Component("core9_dcache", "memHierarchy.Cache")
core9_dcache.addParams({
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
})

core9_ccache = sst.Component("core9_ccache", "memHierarchy.Cache")
core9_ccache.addParams({
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
})

core9_tcache = sst.Component("core9_tcache", "memHierarchy.Cache")
core9_tcache.addParams({
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
})


########################################
# Core 10

# Interfaces
macsim_icache_if_10 = macsim.setSubComponent("core10_icache", "memHierarchy.standardInterface")
macsim_icache_if_10.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_10 = macsim.setSubComponent("core10_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_10.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_10 = macsim.setSubComponent("core10_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_10.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_10 = macsim.setSubComponent("core10_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_10.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core10_icache = sst.Component("core10_icache", "memHierarchy.Cache")
core10_icache.addParams({
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
})

core10_dcache = sst.Component("core10_dcache", "memHierarchy.Cache")
core10_dcache.addParams({
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
})

core10_ccache = sst.Component("core10_ccache", "memHierarchy.Cache")
core10_ccache.addParams({
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
})

core10_tcache = sst.Component("core10_tcache", "memHierarchy.Cache")
core10_tcache.addParams({
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
})


########################################
# Core 11

# Interfaces
macsim_icache_if_11 = macsim.setSubComponent("core11_icache", "memHierarchy.standardInterface")
macsim_icache_if_11.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_11 = macsim.setSubComponent("core11_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_11.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_11 = macsim.setSubComponent("core11_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_11.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_11 = macsim.setSubComponent("core11_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_11.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core11_icache = sst.Component("core11_icache", "memHierarchy.Cache")
core11_icache.addParams({
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
})

core11_dcache = sst.Component("core11_dcache", "memHierarchy.Cache")
core11_dcache.addParams({
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
})

core11_ccache = sst.Component("core11_ccache", "memHierarchy.Cache")
core11_ccache.addParams({
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
})

core11_tcache = sst.Component("core11_tcache", "memHierarchy.Cache")
core11_tcache.addParams({
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
})


########################################
# Core 12

# Interfaces
macsim_icache_if_12 = macsim.setSubComponent("core12_icache", "memHierarchy.standardInterface")
macsim_icache_if_12.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_12 = macsim.setSubComponent("core12_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_12.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_12 = macsim.setSubComponent("core12_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_12.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_12 = macsim.setSubComponent("core12_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_12.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core12_icache = sst.Component("core12_icache", "memHierarchy.Cache")
core12_icache.addParams({
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
})

core12_dcache = sst.Component("core12_dcache", "memHierarchy.Cache")
core12_dcache.addParams({
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
})

core12_ccache = sst.Component("core12_ccache", "memHierarchy.Cache")
core12_ccache.addParams({
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
})

core12_tcache = sst.Component("core12_tcache", "memHierarchy.Cache")
core12_tcache.addParams({
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
})


########################################
# Core 13

# Interfaces
macsim_icache_if_13 = macsim.setSubComponent("core13_icache", "memHierarchy.standardInterface")
macsim_icache_if_13.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_13 = macsim.setSubComponent("core13_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_13.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_13 = macsim.setSubComponent("core13_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_13.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_13 = macsim.setSubComponent("core13_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_13.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core13_icache = sst.Component("core13_icache", "memHierarchy.Cache")
core13_icache.addParams({
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
})

core13_dcache = sst.Component("core13_dcache", "memHierarchy.Cache")
core13_dcache.addParams({
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
})

core13_ccache = sst.Component("core13_ccache", "memHierarchy.Cache")
core13_ccache.addParams({
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
})

core13_tcache = sst.Component("core13_tcache", "memHierarchy.Cache")
core13_tcache.addParams({
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
})


########################################
# Core 14

# Interfaces
macsim_icache_if_14 = macsim.setSubComponent("core14_icache", "memHierarchy.standardInterface")
macsim_icache_if_14.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_14 = macsim.setSubComponent("core14_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_14.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_14 = macsim.setSubComponent("core14_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_14.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_14 = macsim.setSubComponent("core14_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_14.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core14_icache = sst.Component("core14_icache", "memHierarchy.Cache")
core14_icache.addParams({
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
})

core14_dcache = sst.Component("core14_dcache", "memHierarchy.Cache")
core14_dcache.addParams({
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
})

core14_ccache = sst.Component("core14_ccache", "memHierarchy.Cache")
core14_ccache.addParams({
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
})

core14_tcache = sst.Component("core14_tcache", "memHierarchy.Cache")
core14_tcache.addParams({
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
})


########################################
# Core 15

# Interfaces
macsim_icache_if_15 = macsim.setSubComponent("core15_icache", "memHierarchy.standardInterface")
macsim_icache_if_15.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_dcache_if_15 = macsim.setSubComponent("core15_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_15.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': VERBOSE
})
macsim_ccache_if_15 = macsim.setSubComponent("core15_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_15.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})
macsim_tcache_if_15 = macsim.setSubComponent("core15_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_15.addParams({
    'debug': DEBUG_LINKS,
    'debug_level': DEBUG_LEVEL,
    'verbose': 10
})

########################################
# L1 Caches
core15_icache = sst.Component("core15_icache", "memHierarchy.Cache")
core15_icache.addParams({
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
})

core15_dcache = sst.Component("core15_dcache", "memHierarchy.Cache")
core15_dcache.addParams({
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
})

core15_ccache = sst.Component("core15_ccache", "memHierarchy.Cache")
core15_ccache.addParams({
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
})

core15_tcache = sst.Component("core15_tcache", "memHierarchy.Cache")
core15_tcache.addParams({
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
})


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


# Links for Core 0
link_macsim_icache_0 = sst.Link("link_macsim_icache_0")
link_macsim_icache_0.connect((macsim_icache_if_0, "port", "1000ps"), (core0_icache, "high_network_0", "1000ps"))

link_macsim_dcache_0 = sst.Link("link_macsim_dcache_0")
link_macsim_dcache_0.connect((macsim_dcache_if_0, "port", "1000ps"), (core0_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_0 = sst.Link("link_macsim_ccache_0")
link_macsim_ccache_0.connect((macsim_ccache_if_0, "port", "1000ps"), (core0_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_0 = sst.Link("link_macsim_tcache_0")
link_macsim_tcache_0.connect((macsim_tcache_if_0, "port", "1000ps"), (core0_tcache, "high_network_0", "1000ps"))


# Links for Core 1
link_macsim_icache_1 = sst.Link("link_macsim_icache_1")
link_macsim_icache_1.connect((macsim_icache_if_1, "port", "1000ps"), (core1_icache, "high_network_0", "1000ps"))

link_macsim_dcache_1 = sst.Link("link_macsim_dcache_1")
link_macsim_dcache_1.connect((macsim_dcache_if_1, "port", "1000ps"), (core1_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_1 = sst.Link("link_macsim_ccache_1")
link_macsim_ccache_1.connect((macsim_ccache_if_1, "port", "1000ps"), (core1_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_1 = sst.Link("link_macsim_tcache_1")
link_macsim_tcache_1.connect((macsim_tcache_if_1, "port", "1000ps"), (core1_tcache, "high_network_0", "1000ps"))


# Links for Core 2
link_macsim_icache_2 = sst.Link("link_macsim_icache_2")
link_macsim_icache_2.connect((macsim_icache_if_2, "port", "1000ps"), (core2_icache, "high_network_0", "1000ps"))

link_macsim_dcache_2 = sst.Link("link_macsim_dcache_2")
link_macsim_dcache_2.connect((macsim_dcache_if_2, "port", "1000ps"), (core2_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_2 = sst.Link("link_macsim_ccache_2")
link_macsim_ccache_2.connect((macsim_ccache_if_2, "port", "1000ps"), (core2_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_2 = sst.Link("link_macsim_tcache_2")
link_macsim_tcache_2.connect((macsim_tcache_if_2, "port", "1000ps"), (core2_tcache, "high_network_0", "1000ps"))


# Links for Core 3
link_macsim_icache_3 = sst.Link("link_macsim_icache_3")
link_macsim_icache_3.connect((macsim_icache_if_3, "port", "1000ps"), (core3_icache, "high_network_0", "1000ps"))

link_macsim_dcache_3 = sst.Link("link_macsim_dcache_3")
link_macsim_dcache_3.connect((macsim_dcache_if_3, "port", "1000ps"), (core3_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_3 = sst.Link("link_macsim_ccache_3")
link_macsim_ccache_3.connect((macsim_ccache_if_3, "port", "1000ps"), (core3_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_3 = sst.Link("link_macsim_tcache_3")
link_macsim_tcache_3.connect((macsim_tcache_if_3, "port", "1000ps"), (core3_tcache, "high_network_0", "1000ps"))


# Links for Core 4
link_macsim_icache_4 = sst.Link("link_macsim_icache_4")
link_macsim_icache_4.connect((macsim_icache_if_4, "port", "1000ps"), (core4_icache, "high_network_0", "1000ps"))

link_macsim_dcache_4 = sst.Link("link_macsim_dcache_4")
link_macsim_dcache_4.connect((macsim_dcache_if_4, "port", "1000ps"), (core4_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_4 = sst.Link("link_macsim_ccache_4")
link_macsim_ccache_4.connect((macsim_ccache_if_4, "port", "1000ps"), (core4_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_4 = sst.Link("link_macsim_tcache_4")
link_macsim_tcache_4.connect((macsim_tcache_if_4, "port", "1000ps"), (core4_tcache, "high_network_0", "1000ps"))


# Links for Core 5
link_macsim_icache_5 = sst.Link("link_macsim_icache_5")
link_macsim_icache_5.connect((macsim_icache_if_5, "port", "1000ps"), (core5_icache, "high_network_0", "1000ps"))

link_macsim_dcache_5 = sst.Link("link_macsim_dcache_5")
link_macsim_dcache_5.connect((macsim_dcache_if_5, "port", "1000ps"), (core5_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_5 = sst.Link("link_macsim_ccache_5")
link_macsim_ccache_5.connect((macsim_ccache_if_5, "port", "1000ps"), (core5_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_5 = sst.Link("link_macsim_tcache_5")
link_macsim_tcache_5.connect((macsim_tcache_if_5, "port", "1000ps"), (core5_tcache, "high_network_0", "1000ps"))


# Links for Core 6
link_macsim_icache_6 = sst.Link("link_macsim_icache_6")
link_macsim_icache_6.connect((macsim_icache_if_6, "port", "1000ps"), (core6_icache, "high_network_0", "1000ps"))

link_macsim_dcache_6 = sst.Link("link_macsim_dcache_6")
link_macsim_dcache_6.connect((macsim_dcache_if_6, "port", "1000ps"), (core6_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_6 = sst.Link("link_macsim_ccache_6")
link_macsim_ccache_6.connect((macsim_ccache_if_6, "port", "1000ps"), (core6_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_6 = sst.Link("link_macsim_tcache_6")
link_macsim_tcache_6.connect((macsim_tcache_if_6, "port", "1000ps"), (core6_tcache, "high_network_0", "1000ps"))


# Links for Core 7
link_macsim_icache_7 = sst.Link("link_macsim_icache_7")
link_macsim_icache_7.connect((macsim_icache_if_7, "port", "1000ps"), (core7_icache, "high_network_0", "1000ps"))

link_macsim_dcache_7 = sst.Link("link_macsim_dcache_7")
link_macsim_dcache_7.connect((macsim_dcache_if_7, "port", "1000ps"), (core7_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_7 = sst.Link("link_macsim_ccache_7")
link_macsim_ccache_7.connect((macsim_ccache_if_7, "port", "1000ps"), (core7_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_7 = sst.Link("link_macsim_tcache_7")
link_macsim_tcache_7.connect((macsim_tcache_if_7, "port", "1000ps"), (core7_tcache, "high_network_0", "1000ps"))


# Links for Core 8
link_macsim_icache_8 = sst.Link("link_macsim_icache_8")
link_macsim_icache_8.connect((macsim_icache_if_8, "port", "1000ps"), (core8_icache, "high_network_0", "1000ps"))

link_macsim_dcache_8 = sst.Link("link_macsim_dcache_8")
link_macsim_dcache_8.connect((macsim_dcache_if_8, "port", "1000ps"), (core8_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_8 = sst.Link("link_macsim_ccache_8")
link_macsim_ccache_8.connect((macsim_ccache_if_8, "port", "1000ps"), (core8_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_8 = sst.Link("link_macsim_tcache_8")
link_macsim_tcache_8.connect((macsim_tcache_if_8, "port", "1000ps"), (core8_tcache, "high_network_0", "1000ps"))


# Links for Core 9
link_macsim_icache_9 = sst.Link("link_macsim_icache_9")
link_macsim_icache_9.connect((macsim_icache_if_9, "port", "1000ps"), (core9_icache, "high_network_0", "1000ps"))

link_macsim_dcache_9 = sst.Link("link_macsim_dcache_9")
link_macsim_dcache_9.connect((macsim_dcache_if_9, "port", "1000ps"), (core9_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_9 = sst.Link("link_macsim_ccache_9")
link_macsim_ccache_9.connect((macsim_ccache_if_9, "port", "1000ps"), (core9_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_9 = sst.Link("link_macsim_tcache_9")
link_macsim_tcache_9.connect((macsim_tcache_if_9, "port", "1000ps"), (core9_tcache, "high_network_0", "1000ps"))


# Links for Core 10
link_macsim_icache_10 = sst.Link("link_macsim_icache_10")
link_macsim_icache_10.connect((macsim_icache_if_10, "port", "1000ps"), (core10_icache, "high_network_0", "1000ps"))

link_macsim_dcache_10 = sst.Link("link_macsim_dcache_10")
link_macsim_dcache_10.connect((macsim_dcache_if_10, "port", "1000ps"), (core10_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_10 = sst.Link("link_macsim_ccache_10")
link_macsim_ccache_10.connect((macsim_ccache_if_10, "port", "1000ps"), (core10_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_10 = sst.Link("link_macsim_tcache_10")
link_macsim_tcache_10.connect((macsim_tcache_if_10, "port", "1000ps"), (core10_tcache, "high_network_0", "1000ps"))


# Links for Core 11
link_macsim_icache_11 = sst.Link("link_macsim_icache_11")
link_macsim_icache_11.connect((macsim_icache_if_11, "port", "1000ps"), (core11_icache, "high_network_0", "1000ps"))

link_macsim_dcache_11 = sst.Link("link_macsim_dcache_11")
link_macsim_dcache_11.connect((macsim_dcache_if_11, "port", "1000ps"), (core11_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_11 = sst.Link("link_macsim_ccache_11")
link_macsim_ccache_11.connect((macsim_ccache_if_11, "port", "1000ps"), (core11_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_11 = sst.Link("link_macsim_tcache_11")
link_macsim_tcache_11.connect((macsim_tcache_if_11, "port", "1000ps"), (core11_tcache, "high_network_0", "1000ps"))


# Links for Core 12
link_macsim_icache_12 = sst.Link("link_macsim_icache_12")
link_macsim_icache_12.connect((macsim_icache_if_12, "port", "1000ps"), (core12_icache, "high_network_0", "1000ps"))

link_macsim_dcache_12 = sst.Link("link_macsim_dcache_12")
link_macsim_dcache_12.connect((macsim_dcache_if_12, "port", "1000ps"), (core12_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_12 = sst.Link("link_macsim_ccache_12")
link_macsim_ccache_12.connect((macsim_ccache_if_12, "port", "1000ps"), (core12_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_12 = sst.Link("link_macsim_tcache_12")
link_macsim_tcache_12.connect((macsim_tcache_if_12, "port", "1000ps"), (core12_tcache, "high_network_0", "1000ps"))


# Links for Core 13
link_macsim_icache_13 = sst.Link("link_macsim_icache_13")
link_macsim_icache_13.connect((macsim_icache_if_13, "port", "1000ps"), (core13_icache, "high_network_0", "1000ps"))

link_macsim_dcache_13 = sst.Link("link_macsim_dcache_13")
link_macsim_dcache_13.connect((macsim_dcache_if_13, "port", "1000ps"), (core13_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_13 = sst.Link("link_macsim_ccache_13")
link_macsim_ccache_13.connect((macsim_ccache_if_13, "port", "1000ps"), (core13_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_13 = sst.Link("link_macsim_tcache_13")
link_macsim_tcache_13.connect((macsim_tcache_if_13, "port", "1000ps"), (core13_tcache, "high_network_0", "1000ps"))


# Links for Core 14
link_macsim_icache_14 = sst.Link("link_macsim_icache_14")
link_macsim_icache_14.connect((macsim_icache_if_14, "port", "1000ps"), (core14_icache, "high_network_0", "1000ps"))

link_macsim_dcache_14 = sst.Link("link_macsim_dcache_14")
link_macsim_dcache_14.connect((macsim_dcache_if_14, "port", "1000ps"), (core14_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_14 = sst.Link("link_macsim_ccache_14")
link_macsim_ccache_14.connect((macsim_ccache_if_14, "port", "1000ps"), (core14_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_14 = sst.Link("link_macsim_tcache_14")
link_macsim_tcache_14.connect((macsim_tcache_if_14, "port", "1000ps"), (core14_tcache, "high_network_0", "1000ps"))


# Links for Core 15
link_macsim_icache_15 = sst.Link("link_macsim_icache_15")
link_macsim_icache_15.connect((macsim_icache_if_15, "port", "1000ps"), (core15_icache, "high_network_0", "1000ps"))

link_macsim_dcache_15 = sst.Link("link_macsim_dcache_15")
link_macsim_dcache_15.connect((macsim_dcache_if_15, "port", "1000ps"), (core15_dcache, "high_network_0", "1000ps"))

link_macsim_ccache_15 = sst.Link("link_macsim_ccache_15")
link_macsim_ccache_15.connect((macsim_ccache_if_15, "port", "1000ps"), (core15_ccache, "high_network_0", "1000ps"))

link_macsim_tcache_15 = sst.Link("link_macsim_tcache_15")
link_macsim_tcache_15.connect((macsim_tcache_if_15, "port", "1000ps"), (core15_tcache, "high_network_0", "1000ps"))


# Links bus for Core 0
link_icache_bus_0 = sst.Link("link_icache_bus_0")
link_icache_bus_0.connect((core0_icache, "low_network_0", "50ps"), (mem_bus, "high_network_0", "50ps"))

link_dcache_bus_0 = sst.Link("link_dcache_bus_0")
link_dcache_bus_0.connect((core0_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_1", "50ps"))

link_ccache_bus_0 = sst.Link("link_ccache_bus_0")
link_ccache_bus_0.connect((core0_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_2", "50ps"))

link_tcache_bus_0 = sst.Link("link_tcache_bus_0")
link_tcache_bus_0.connect((core0_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_3", "50ps"))


# Links bus for Core 1
link_icache_bus_1 = sst.Link("link_icache_bus_1")
link_icache_bus_1.connect((core1_icache, "low_network_0", "50ps"), (mem_bus, "high_network_4", "50ps"))

link_dcache_bus_1 = sst.Link("link_dcache_bus_1")
link_dcache_bus_1.connect((core1_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_5", "50ps"))

link_ccache_bus_1 = sst.Link("link_ccache_bus_1")
link_ccache_bus_1.connect((core1_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_6", "50ps"))

link_tcache_bus_1 = sst.Link("link_tcache_bus_1")
link_tcache_bus_1.connect((core1_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_7", "50ps"))


# Links bus for Core 2
link_icache_bus_2 = sst.Link("link_icache_bus_2")
link_icache_bus_2.connect((core2_icache, "low_network_0", "50ps"), (mem_bus, "high_network_8", "50ps"))

link_dcache_bus_2 = sst.Link("link_dcache_bus_2")
link_dcache_bus_2.connect((core2_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_9", "50ps"))

link_ccache_bus_2 = sst.Link("link_ccache_bus_2")
link_ccache_bus_2.connect((core2_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_10", "50ps"))

link_tcache_bus_2 = sst.Link("link_tcache_bus_2")
link_tcache_bus_2.connect((core2_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_11", "50ps"))


# Links bus for Core 3
link_icache_bus_3 = sst.Link("link_icache_bus_3")
link_icache_bus_3.connect((core3_icache, "low_network_0", "50ps"), (mem_bus, "high_network_12", "50ps"))

link_dcache_bus_3 = sst.Link("link_dcache_bus_3")
link_dcache_bus_3.connect((core3_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_13", "50ps"))

link_ccache_bus_3 = sst.Link("link_ccache_bus_3")
link_ccache_bus_3.connect((core3_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_14", "50ps"))

link_tcache_bus_3 = sst.Link("link_tcache_bus_3")
link_tcache_bus_3.connect((core3_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_15", "50ps"))


# Links bus for Core 4
link_icache_bus_4 = sst.Link("link_icache_bus_4")
link_icache_bus_4.connect((core4_icache, "low_network_0", "50ps"), (mem_bus, "high_network_16", "50ps"))

link_dcache_bus_4 = sst.Link("link_dcache_bus_4")
link_dcache_bus_4.connect((core4_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_17", "50ps"))

link_ccache_bus_4 = sst.Link("link_ccache_bus_4")
link_ccache_bus_4.connect((core4_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_18", "50ps"))

link_tcache_bus_4 = sst.Link("link_tcache_bus_4")
link_tcache_bus_4.connect((core4_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_19", "50ps"))


# Links bus for Core 5
link_icache_bus_5 = sst.Link("link_icache_bus_5")
link_icache_bus_5.connect((core5_icache, "low_network_0", "50ps"), (mem_bus, "high_network_20", "50ps"))

link_dcache_bus_5 = sst.Link("link_dcache_bus_5")
link_dcache_bus_5.connect((core5_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_21", "50ps"))

link_ccache_bus_5 = sst.Link("link_ccache_bus_5")
link_ccache_bus_5.connect((core5_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_22", "50ps"))

link_tcache_bus_5 = sst.Link("link_tcache_bus_5")
link_tcache_bus_5.connect((core5_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_23", "50ps"))


# Links bus for Core 6
link_icache_bus_6 = sst.Link("link_icache_bus_6")
link_icache_bus_6.connect((core6_icache, "low_network_0", "50ps"), (mem_bus, "high_network_24", "50ps"))

link_dcache_bus_6 = sst.Link("link_dcache_bus_6")
link_dcache_bus_6.connect((core6_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_25", "50ps"))

link_ccache_bus_6 = sst.Link("link_ccache_bus_6")
link_ccache_bus_6.connect((core6_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_26", "50ps"))

link_tcache_bus_6 = sst.Link("link_tcache_bus_6")
link_tcache_bus_6.connect((core6_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_27", "50ps"))


# Links bus for Core 7
link_icache_bus_7 = sst.Link("link_icache_bus_7")
link_icache_bus_7.connect((core7_icache, "low_network_0", "50ps"), (mem_bus, "high_network_28", "50ps"))

link_dcache_bus_7 = sst.Link("link_dcache_bus_7")
link_dcache_bus_7.connect((core7_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_29", "50ps"))

link_ccache_bus_7 = sst.Link("link_ccache_bus_7")
link_ccache_bus_7.connect((core7_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_30", "50ps"))

link_tcache_bus_7 = sst.Link("link_tcache_bus_7")
link_tcache_bus_7.connect((core7_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_31", "50ps"))


# Links bus for Core 8
link_icache_bus_8 = sst.Link("link_icache_bus_8")
link_icache_bus_8.connect((core8_icache, "low_network_0", "50ps"), (mem_bus, "high_network_32", "50ps"))

link_dcache_bus_8 = sst.Link("link_dcache_bus_8")
link_dcache_bus_8.connect((core8_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_33", "50ps"))

link_ccache_bus_8 = sst.Link("link_ccache_bus_8")
link_ccache_bus_8.connect((core8_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_34", "50ps"))

link_tcache_bus_8 = sst.Link("link_tcache_bus_8")
link_tcache_bus_8.connect((core8_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_35", "50ps"))


# Links bus for Core 9
link_icache_bus_9 = sst.Link("link_icache_bus_9")
link_icache_bus_9.connect((core9_icache, "low_network_0", "50ps"), (mem_bus, "high_network_36", "50ps"))

link_dcache_bus_9 = sst.Link("link_dcache_bus_9")
link_dcache_bus_9.connect((core9_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_37", "50ps"))

link_ccache_bus_9 = sst.Link("link_ccache_bus_9")
link_ccache_bus_9.connect((core9_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_38", "50ps"))

link_tcache_bus_9 = sst.Link("link_tcache_bus_9")
link_tcache_bus_9.connect((core9_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_39", "50ps"))


# Links bus for Core 10
link_icache_bus_10 = sst.Link("link_icache_bus_10")
link_icache_bus_10.connect((core10_icache, "low_network_0", "50ps"), (mem_bus, "high_network_40", "50ps"))

link_dcache_bus_10 = sst.Link("link_dcache_bus_10")
link_dcache_bus_10.connect((core10_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_41", "50ps"))

link_ccache_bus_10 = sst.Link("link_ccache_bus_10")
link_ccache_bus_10.connect((core10_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_42", "50ps"))

link_tcache_bus_10 = sst.Link("link_tcache_bus_10")
link_tcache_bus_10.connect((core10_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_43", "50ps"))


# Links bus for Core 11
link_icache_bus_11 = sst.Link("link_icache_bus_11")
link_icache_bus_11.connect((core11_icache, "low_network_0", "50ps"), (mem_bus, "high_network_44", "50ps"))

link_dcache_bus_11 = sst.Link("link_dcache_bus_11")
link_dcache_bus_11.connect((core11_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_45", "50ps"))

link_ccache_bus_11 = sst.Link("link_ccache_bus_11")
link_ccache_bus_11.connect((core11_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_46", "50ps"))

link_tcache_bus_11 = sst.Link("link_tcache_bus_11")
link_tcache_bus_11.connect((core11_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_47", "50ps"))


# Links bus for Core 12
link_icache_bus_12 = sst.Link("link_icache_bus_12")
link_icache_bus_12.connect((core12_icache, "low_network_0", "50ps"), (mem_bus, "high_network_48", "50ps"))

link_dcache_bus_12 = sst.Link("link_dcache_bus_12")
link_dcache_bus_12.connect((core12_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_49", "50ps"))

link_ccache_bus_12 = sst.Link("link_ccache_bus_12")
link_ccache_bus_12.connect((core12_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_50", "50ps"))

link_tcache_bus_12 = sst.Link("link_tcache_bus_12")
link_tcache_bus_12.connect((core12_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_51", "50ps"))


# Links bus for Core 13
link_icache_bus_13 = sst.Link("link_icache_bus_13")
link_icache_bus_13.connect((core13_icache, "low_network_0", "50ps"), (mem_bus, "high_network_52", "50ps"))

link_dcache_bus_13 = sst.Link("link_dcache_bus_13")
link_dcache_bus_13.connect((core13_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_53", "50ps"))

link_ccache_bus_13 = sst.Link("link_ccache_bus_13")
link_ccache_bus_13.connect((core13_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_54", "50ps"))

link_tcache_bus_13 = sst.Link("link_tcache_bus_13")
link_tcache_bus_13.connect((core13_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_55", "50ps"))


# Links bus for Core 14
link_icache_bus_14 = sst.Link("link_icache_bus_14")
link_icache_bus_14.connect((core14_icache, "low_network_0", "50ps"), (mem_bus, "high_network_56", "50ps"))

link_dcache_bus_14 = sst.Link("link_dcache_bus_14")
link_dcache_bus_14.connect((core14_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_57", "50ps"))

link_ccache_bus_14 = sst.Link("link_ccache_bus_14")
link_ccache_bus_14.connect((core14_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_58", "50ps"))

link_tcache_bus_14 = sst.Link("link_tcache_bus_14")
link_tcache_bus_14.connect((core14_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_59", "50ps"))


# Links bus for Core 15
link_icache_bus_15 = sst.Link("link_icache_bus_15")
link_icache_bus_15.connect((core15_icache, "low_network_0", "50ps"), (mem_bus, "high_network_60", "50ps"))

link_dcache_bus_15 = sst.Link("link_dcache_bus_15")
link_dcache_bus_15.connect((core15_dcache, "low_network_0", "50ps"), (mem_bus, "high_network_61", "50ps"))

link_ccache_bus_15 = sst.Link("link_ccache_bus_15")
link_ccache_bus_15.connect((core15_ccache, "low_network_0", "50ps"), (mem_bus, "high_network_62", "50ps"))

link_tcache_bus_15 = sst.Link("link_tcache_bus_15")
link_tcache_bus_15.connect((core15_tcache, "low_network_0", "50ps"), (mem_bus, "high_network_63", "50ps"))

# Bus -> Memory
link_bus_mem = sst.Link("link_bus_mem")
link_bus_mem.connect( (mem_bus, "low_network_0", "50ps"), (memctrl, "direct_link", "50ps") )


########################################
# Enable statistics
sst.setStatisticLoadLevel(7)
sst.setStatisticOutput("sst.statOutputConsole")
