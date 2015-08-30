g,n,c=""," ",""
for i in"51g7h50g10h49g11h48g13h48g13g4g3h48g12g1g11h48g25h49g25h34g8g8g25h32g10g10g22h29g13g11g21h29g13g10g20h23g24g4g7g2g10h19g38h16g40h14g44h13g46h12g48h11g49h10g51h10g52h9g13g3g15g3g19h9g10g3g4g2g9g2g4g2g17h9g10g1g8g1g6g2g8g1g16h10g8g1g9g1g6g1g9g2g15h10g8g1g10g1g5g1g10g1g15h10g8g1g10g1g5g1g10g1g15h8g10g1g10g1g5g1g10g1g17h7g11g1g9g1g6g1g10g1g19h6g13g1g8g1g7g2g7g2g20h5g16g6g11g7g22h4g63h4g63h4g63h4g63h5g61h6g59h7g58h8g56h9g53h12g48h16g39h":
 if i=="g":
  g+=n*int(c);c=""
  n="*"if n is" "else" "
 elif i=="h":
  g+=n*int(c)
  c,n=""," "
  g+="\n"
 else:c+=i
print(g)