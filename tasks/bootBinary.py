import logging
from core.task import Task
from core.parameter import Parameter

class BootBinary(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="bootBinary", after="build")

        self.fsbl = Parameter(name = "fsbl",
                              example = "zynqmp_fsbl.elf",
                              description = "optional")

        self.fpga = Parameter(name = "fpga",
                              example = "fpga.bit",
                              description = "optional")

        self.atf = Parameter(name = "atf",
                             example = "bl31.elf",
                             description = "optional")

        self.uboot = Parameter(name = "uboot",
                               example = "u-boot.elf",
                               description = "optional")

        self.pmufw = Parameter(name = "pmufw",
                               example = "pmufw.elf",
                               description = "optional")

        self.rpu = Parameter(name = "rpu",
                             example = "test.elf",
                             description = "optional")

        self.init = Parameter(name = "init",
                              example = "regs.init",
                              description = "optional")

        self.addParameterWithParent(["binary"], self.fsbl)
        self.addParameterWithParent(["binary"], self.fpga)
        self.addParameterWithParent(["binary"], self.atf)
        self.addParameterWithParent(["binary"], self.uboot)
        self.addParameterWithParent(["binary"], self.pmufw)
        self.addParameterWithParent(["binary"], self.rpu)
        self.addParameterWithParent(["binary"], self.init)


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

