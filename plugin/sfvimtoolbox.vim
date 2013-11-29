if !has('python')
  echo "Error: Required vim complied with +python"
  finish
endif

let s:scriptfile = fnameescape(fnamemodify(expand("<sfile>"),":h"))

exe "pyfile ".fnameescape(fnamemodify(expand("<sfile>"),":h").'/py/sftoolbox.py')
 
function! ToggleSFToolBox()
  
endfunc

fun CompileSCSS()
  py sf_process_scss()
endfun

autocmd BufWritePost *.scss call CompileSCSS()

command! TSF call ToggleSFToolBox()

