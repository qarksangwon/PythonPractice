# class 클래스명:
# 생성자는 __init__ 이므로,
# def __init__(param1,param2,param3)
# 자바의 this -> 파이썬의 self
# 파이썬은 데이터 타입을 지정하지 않아서 오버로딩이 없다!

class ProtoTV:
    def __init__(self, isOn, channel, volume):
        self.isOn = isOn
        self.channel = channel
        self.volume = volume
    def set_on(self, isOn):
        self.isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else :
            print(f"채널 설정 범위가 아닙니다.")
    def set_volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.isOn
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume

lg_tv = ProtoTV("True","10","10")
print(lg_tv.isOn)
print(lg_tv.volume)


# 상속
# 오버라이딩 : 그냥 동일하게 재정의해서 하면됨
class TV(ProtoTV):
    def set_channel(self, cnl):
        if 0 < cnl < 2000 :
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else :
            print(f"채널 설정 범위가 아닙니다.")

lg_tv = TV(False, 10, 10)
samsung_tv = TV(False, 20, 20)
samsung_tv.set_channel(1200)

proto = ProtoTV(False, 10, 10)
proto.set_channel(1000)