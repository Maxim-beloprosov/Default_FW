from Test.mobile.mobile_base import MobileBase


class TestTemp(MobileBase):

    def test_temp(self):
        self.APP.appium_instance.get_Appium_Driver_Instance()