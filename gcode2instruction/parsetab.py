
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'G0 G1 POSE POSX POSY POSZ SPEED t_ignore_COMMENTSinstrucions : instrucions instrucioninstrucions : instrucion instrucioninstrucion : G1 parametersinstrucion : G0 parametersparameters : SPEED POSX POSY POSEparameters : SPEED POSX POSY POSZparameters : SPEED POSX POSYparameters : SPEED POSEparameters : POSX POSY POSEparameters : POSX POSY'
    
_lr_action_items = {'G1':([0,1,2,5,6,7,10,12,13,14,15,16,17,],[3,3,3,-1,-2,-3,-4,-8,-10,-7,-9,-5,-6,]),'G0':([0,1,2,5,6,7,10,12,13,14,15,16,17,],[4,4,4,-1,-2,-3,-4,-8,-10,-7,-9,-5,-6,]),'$end':([1,5,6,7,10,12,13,14,15,16,17,],[0,-1,-2,-3,-4,-8,-10,-7,-9,-5,-6,]),'SPEED':([3,4,],[8,8,]),'POSX':([3,4,8,],[9,9,11,]),'POSE':([8,13,14,],[12,15,16,]),'POSY':([9,11,],[13,14,]),'POSZ':([14,],[17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucions':([0,],[1,]),'instrucion':([0,1,2,],[2,5,6,]),'parameters':([3,4,],[7,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucions","S'",1,None,None,None),
  ('instrucions -> instrucions instrucion','instrucions',2,'p_instrutions_1','yacc.py',17),
  ('instrucions -> instrucion instrucion','instrucions',2,'p_instrutions_2','yacc.py',22),
  ('instrucion -> G1 parameters','instrucion',2,'p_instrution_1','yacc.py',29),
  ('instrucion -> G0 parameters','instrucion',2,'p_instrution_2','yacc.py',34),
  ('parameters -> SPEED POSX POSY POSE','parameters',4,'p_parameters_1','yacc.py',41),
  ('parameters -> SPEED POSX POSY POSZ','parameters',4,'p_parameters_2','yacc.py',48),
  ('parameters -> SPEED POSX POSY','parameters',3,'p_parameters_3','yacc.py',54),
  ('parameters -> SPEED POSE','parameters',2,'p_parameters_4','yacc.py',60),
  ('parameters -> POSX POSY POSE','parameters',3,'p_parameters_5','yacc.py',67),
  ('parameters -> POSX POSY','parameters',2,'p_parameters_6','yacc.py',74),
]
