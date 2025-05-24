################################################################################
# Description: 
#  - Macsim is connected to 2 individual memory controllers for instruction and
#    data memory.
#  - Macsim ports (stdInterface) are loaded as subcomponents explictly.
################################################################################
import sst
from common import *

# 0: None, 1: Stdout, 2: Stderr, 3: File
DEBUG_CORE          = 1
DEBUG_CORE_LINKS    = 1
DEBUG_L1            = 0
DEBUG_MEM           = 0

DEBUG_LINKS         = 0
DEBUG_BUS           = 0

DEBUG_LEVEL         = 5
VERBOSE             = 10

########################################
# System Parameters
MEM_SIZE_S = '512MiB'
MEM_SIZE = str2bytes(MEM_SIZE_S)
MEM_START = 0
MEM_END = MEM_START + MEM_SIZE - 1


########################################
# Macsim
macsim = sst.Component("macsimComponent", "macsimComponent.macsimComponent")
macsim.addParams({
    "param_file": "params.in",
    "trace_file": "trace_file_list_yolo",
    "output_dir": "output_dir",
    "command_line": "--num_sim_cores=2 --num_sim_large_cores=0 --num_sim_small_cores=2 --use_memhierarchy=1 --core_type=nvbit",
    "frequency" : "2GHz",
    "num_cores" : "2",
    "num_link": "2",
    "mem_size" : MEM_SIZE,
    "debug": DEBUG_CORE,
    "debug_level": DEBUG_LEVEL,
})

# Example for cores 0 through 15, with icache, dcache, ccache, and tcache interfaces,
# their corresponding memory controllers, and links.

# --- Core 0 ---
macsim_icache_if_0 = macsim.setSubComponent("core0_icache", "memHierarchy.standardInterface")
macsim_icache_if_0.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })
macsim_dcache_if_0 = macsim.setSubComponent("core0_dcache", "memHierarchy.standardInterface")
macsim_dcache_if_0.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })
macsim_ccache_if_0 = macsim.setSubComponent("core0_ccache", "memHierarchy.standardInterface")
macsim_ccache_if_0.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })
macsim_tcache_if_0 = macsim.setSubComponent("core0_tcache", "memHierarchy.standardInterface")
macsim_tcache_if_0.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })

memctrl_i_0 = sst.Component("memory_i_0", "memHierarchy.MemController")
memctrl_i_0.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "addr_range_end": MEM_END })
memory_i_0 = memctrl_i_0.setSubComponent("backend", "memHierarchy.simpleMem")
memory_i_0.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

memctrl_d_0 = sst.Component("memory_d_0", "memHierarchy.MemController")
memctrl_d_0.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "verbose": VERBOSE, "addr_range_start": MEM_START, "addr_range_end": MEM_END })
memory_d_0 = memctrl_d_0.setSubComponent("backend", "memHierarchy.simpleMem")
memory_d_0.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

memctrl_c_0 = sst.Component("memory_c_0", "memHierarchy.MemController")
memctrl_c_0.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "verbose": VERBOSE, "addr_range_start": MEM_START, "addr_range_end": MEM_END })
memory_c_0 = memctrl_c_0.setSubComponent("backend", "memHierarchy.simpleMem")
memory_c_0.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

memctrl_t_0 = sst.Component("memory_t_0", "memHierarchy.MemController")
memctrl_t_0.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "verbose": VERBOSE, "addr_range_start": MEM_START, "addr_range_end": MEM_END })
memory_t_0 = memctrl_t_0.setSubComponent("backend", "memHierarchy.simpleMem")
memory_t_0.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

link_bus_memctrl_i_0 = sst.Link("link_bus_memctrl_i_0")
link_bus_memctrl_i_0.connect((macsim_icache_if_0, "port", "50ps"), (memctrl_i_0, "direct_link", "50ps"))
link_bus_memctrl_d_0 = sst.Link("link_bus_memctrl_d_0")
link_bus_memctrl_d_0.connect((macsim_dcache_if_0, "port", "50ps"), (memctrl_d_0, "direct_link", "50ps"))
link_bus_memctrl_c_0 = sst.Link("link_bus_memctrl_c_0")
link_bus_memctrl_c_0.connect((macsim_ccache_if_0, "port", "50ps"), (memctrl_c_0, "direct_link", "50ps"))
link_bus_memctrl_t_0 = sst.Link("link_bus_memctrl_t_0")
link_bus_memctrl_t_0.connect((macsim_tcache_if_0, "port", "50ps"), (memctrl_t_0, "direct_link", "50ps"))

# # --- Core 1 ---
# macsim_icache_if_1 = macsim.setSubComponent("core1_icache", "memHierarchy.standardInterface")
# macsim_icache_if_1.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })
# macsim_dcache_if_1 = macsim.setSubComponent("core1_dcache", "memHierarchy.standardInterface")
# macsim_dcache_if_1.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })
# macsim_ccache_if_1 = macsim.setSubComponent("core1_ccache", "memHierarchy.standardInterface")
# macsim_ccache_if_1.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })
# macsim_tcache_if_1 = macsim.setSubComponent("core1_tcache", "memHierarchy.standardInterface")
# macsim_tcache_if_1.addParams({ 'debug': DEBUG_CORE_LINKS, 'debug_level': DEBUG_LEVEL, 'verbose': 10 })

# memctrl_i_1 = sst.Component("memory_i_1", "memHierarchy.MemController")
# memctrl_i_1.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "addr_range_end": MEM_END })
# memory_i_1 = memctrl_i_1.setSubComponent("backend", "memHierarchy.simpleMem")
# memory_i_1.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

# memctrl_d_1 = sst.Component("memory_d_1", "memHierarchy.MemController")
# memctrl_d_1.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "verbose": VERBOSE, "addr_range_start": MEM_START, "addr_range_end": MEM_END })
# memory_d_1 = memctrl_d_1.setSubComponent("backend", "memHierarchy.simpleMem")
# memory_d_1.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

# memctrl_c_1 = sst.Component("memory_c_1", "memHierarchy.MemController")
# memctrl_c_1.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "verbose": VERBOSE, "addr_range_start": MEM_START, "addr_range_end": MEM_END })
# memory_c_1 = memctrl_c_1.setSubComponent("backend", "memHierarchy.simpleMem")
# memory_c_1.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

# memctrl_t_1 = sst.Component("memory_t_1", "memHierarchy.MemController")
# memctrl_t_1.addParams({ "debug": DEBUG_MEM, "debug_level": DEBUG_LEVEL, "clock": "1GHz", "verbose": VERBOSE, "addr_range_start": MEM_START, "addr_range_end": MEM_END })
# memory_t_1 = memctrl_t_1.setSubComponent("backend", "memHierarchy.simpleMem")
# memory_t_1.addParams({ "access_time": "1000ns", "mem_size": MEM_SIZE_S })

# link_bus_memctrl_i_1 = sst.Link("link_bus_memctrl_i_1")
# link_bus_memctrl_i_1.connect((macsim_icache_if_1, "port", "50ps"), (memctrl_i_1, "direct_link", "50ps"))
# link_bus_memctrl_d_1 = sst.Link("link_bus_memctrl_d_1")
# link_bus_memctrl_d_1.connect((macsim_dcache_if_1, "port", "50ps"), (memctrl_d_1, "direct_link", "50ps"))
# link_bus_memctrl_c_1 = sst.Link("link_bus_memctrl_c_1")
# link_bus_memctrl_c_1.connect((macsim_ccache_if_1, "port", "50ps"), (memctrl_c_1, "direct_link", "50ps"))
# link_bus_memctrl_t_1 = sst.Link("link_bus_memctrl_t_1")
# link_bus_memctrl_t_1.connect((macsim_tcache_if_1, "port", "50ps"), (memctrl_t_1, "direct_link", "50ps"))

# Repeat for cores 2 through 15



########################################
# Enable statistics
sst.setStatisticLoadLevel(7)
sst.setStatisticOutput("sst.statOutputConsole")
# sst.setStatisticOutput("sst.statOutputCSV", {"filepath" : "./sst_stats.csv", "separator" : ", " } )

#sst.enableAllStatisticsForComponentType("memHierarchy.MemController")
