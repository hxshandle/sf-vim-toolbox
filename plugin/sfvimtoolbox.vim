if !has('python')
  echo "Error: Required vim complied with +python"
  finish
endif

function! ToggleSFToolBox()
  pyfile 'lib/sftoolbox.py'
endfunc

command! tsf call ToggleSFToolBox()

