if !has('python')
  echo "Error: Required vim complied with +python"
  finish
endif

function! ToggleSFToolBox()
  pyfile py/sftoolbox.py
endfunc

command! TSF call ToggleSFToolBox()

