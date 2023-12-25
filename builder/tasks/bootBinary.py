import logging
from tasks.Itask import ITask
from config.parameter import Parameter
from config.configTree import ConfigTree
from core.sequence import Sequence

class BootBinary(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="bootBinary", after="build")

        self.fsbl = Parameter(name = "fsbl",
                              parent = ["binary"],
                              example = "zynqmp_fsbl.elf",
                              isOptional = True,
                              description = "Path to FSBL binary")

        self.fpga = Parameter(name = "fpga",
                              parent = ["binary"],
                              example = "fpga.bit",
                              isOptional = True,
                              description = "Path to bitstream / no bitstream if missing / default bitstream if empty")

        self.atf = Parameter(name = "atf",
                             parent = ["binary"],
                             example = "bl31.elf",
                             isOptional = True,
                             description = "Path to ATF binary")

        self.uboot = Parameter(name = "uboot",
                               parent = ["binary"],
                               example = "u-boot.elf",
                               isOptional = True,
                               description = "Path to U-Boot binary")

        self.pmufw = Parameter(name = "pmufw",
                               parent = ["binary"],
                               example = "pmufw.elf",
                               isOptional = True,
                               description = "Path to PMU firmware binary")

        self.rpu = Parameter(name = "rpu",
                             parent = ["binary"],
                             example = "test.elf",
                             isOptional = True,
                             description = "Path to binary executed on RPU")

        self.init = Parameter(name = "init",
                              parent = ["binary"],
                              example = "regs.init",
                              isOptional = True,
                              description = "Register initialization file for boot ROM")

        self.addParameter(self.fsbl)
        self.addParameter(self.fpga)
        self.addParameter(self.atf)
        self.addParameter(self.uboot)
        self.addParameter(self.pmufw)
        self.addParameter(self.rpu)
        self.addParameter(self.init)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("fsbl = " + self.fsbl.value)
        logging.debug("fpga = " + self.fpga.value)
        logging.debug("atf = " + self.atf.value)
        logging.debug("uboot = " + self.uboot.value)
        logging.debug("pmufw = " + self.pmufw.value)
        logging.debug("rpu = " + self.rpu.value)
        logging.debug("init = " + self.init.value)
        logging.info("BootBinary executed")


    def clean(self) -> None:
        pass

