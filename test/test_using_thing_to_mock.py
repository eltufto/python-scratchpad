import using_thing_to_mock
import class_to_mock
from mock import patch, MagicMock, call
import pytest
from utils import UdevWrapper
import pyudev

@patch.object(class_to_mock.ClassToMock, 'm1')
@patch.object(class_to_mock.ClassToMock, 'm2')
def test_method_call_order(mock_m2, mock_m1):
    mock_m1.return_value = True
    mock_m2.return_value = True
    
    using_thing_to_mock.myfunc()
    
    assert mock_m1.called
    assert mock_m2.called
    
@patch('class_to_mock.modulem1')
@patch('class_to_mock.modulem2')
def test_method_call_order_module(mock_m2, mock_m1):
    mock_m1.return_value = True
    mock_m2.return_value = True
    
    result = class_to_mock.modulem1()
    class_to_mock.modulem2()
  
    assert mock_m1.called
    assert mock_m2.called
    assert result is True
    
#def test_order():
#    parent = MagicMock()
#    expected_result = ('mock1', 'mock2')
#
#    with patch('class_to_mock.ClassToMock.m1', return_value="mock1") as child1:
#        with patch('class_to_mock.ClassToMock.m2', return_value="mock2") as child2:
#            parent.attach_mock(child1, 'child1')
#            parent.attach_mock(child2, 'child2')
#            child1('one')
#            child2('two')
#            
#            assert using_thing_to_mock.myfunc() == expected_result
#            
#            expected_calls = [call.child1('one'), call.child2('two'), call.child1(), call.child2()]
#    assert parent.mock_calls == expected_calls
#    
#
#
#def test_patch_undone():
#
#    expected_result = ('result1', 'result2')
#
#
#    assert using_thing_to_mock.myfunc() == expected_result
    
#---------------------------------------------------- def test_no_mocking(self):
    #----------------------------------- expected_result = ('result1','result2')
    #-------------------- assert using_thing_to_mock.myfunc() == expected_result


    
#--------------------------------- @patch.object(class_to_mock.ClassToMock,'m2')
#------------------------------------ def test_method_mocked_correctly(mock_m2):
    #------------------------------- expected_result = ('result1','mockresult2')
    #-------------------------------------- mock_m2.return_value = 'mockresult2'
    #-------------------------------- test_result = using_thing_to_mock.myfunc()
    #------------------------------------- assert test_result == expected_result
#------------------------------------------------------------------------------ 
#--------------------------------- @patch.object(class_to_mock.ClassToMock,'m2')
#---------------------------------------------- def test_method_called(mock_m2):
    #-------------------------------------- mock_m2.return_value = 'mockresult2'
    #---------------------------------------------- using_thing_to_mock.myfunc()
    #----------------------------------------------------- assert mock_m2.called
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#---------------------------------------------------------------- def mock_m2():
    #------------------------------------------------ return "monkeymockresult2"
#------------------------------------------------------------------------------ 
#------------------------------------------- def test_with_monkeys(monkeypatch):
    #--------------- monkeypatch.setattr(class_to_mock.ClassToMock,'m2',mock_m2)
    #------------------------- expected_result = ('result1','monkeymockresult2')
    #-------------------------------- test_result = using_thing_to_mock.myfunc()
    #------------------------------------- assert test_result == expected_result

    #------------------------------------------------ def test_udev_stuff(self):
        #----------- device = UdevWrapper.get_device_from_name('tty', 'ttyUSB0')
        #-------------------------- assert device.get('ID_VENDOR') == 'whats up'
#------------------------------------------------------------------------------ 
    #----------------------------------------- @patch('pyudev.Device.from_name')
    #-------------------------------- def test_udev_stuff_mock(self,MockDevice):
        #----------------------- MockDevice.return_value = {'ID_VENDOR': 'blah'}
        #----------- device = UdevWrapper.get_device_from_name('tty', 'ttyUSB0')
        #-------------------------- assert device.get('ID_VENDOR') == 'whats up'
        
