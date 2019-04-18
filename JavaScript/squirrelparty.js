let sparty = (cigars, weekend) => {
  if weekend{
    ((cigars >=40) ? 'We got a party' : 'No party here')
  }else{
    ((cigars >=40) && (cigars <=60)) ? 'We got a party' : 'No party here')
  }
}

let sparty1 = (cigars, weekend) => ((cigars >= 40) && (weekend || (cigars <= 60)) ? 'We got a party' : 'No party here')
