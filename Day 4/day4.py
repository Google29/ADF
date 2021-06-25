import pytest
import ass4
@pytest.mark.parametrize("to,ing,pal,max,uniq,dic",[(1,2,['hannah', 'malayalam', 'lool'],['Google', 'is'],['Google', 'is', 'to', 'Good', 'at', 'farming', 'running', 'hannah', 'malayalam', 'lool'],{1: 'Google', 2: 'is', 3: 'to', 4: 'Good', 5: 'at', 6: 'farming', 7: 'Google', 8: 'is', 9: 'running', 10: 'hannah', 11: 'malayalam', 12: 'lool'})])
def testing(to,ing,max,pal,uniq,dic):
    assert to==ass4.TO
    assert ing==ass4.ING
    assert max==ass4.maxList
    assert pal==ass4.palindrome
    assert uniq==ass4.uniqueList
    assert dic==ass4.Word
