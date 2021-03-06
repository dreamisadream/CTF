  難度 :  :star: :star: :star: 
  
  漏洞:

  - Fill 存在 heap overflow <br>
       
           
   ---
  
  解題流程:
           
 * 概略 
           先用 partial fastbin attack leak 出 libc_base <br>
           再修改 free_hook 成 system <br>
          最後再 free 掉內容為 /bin/sh 的 chunk <br>
  
 * 詳細介紹
   * <b>先用 partial fastbin attack leak 出 libc_base</b><br>
     為了要 leak 出 libc_base 我們得先將 tcache 填滿, 這樣才能夠 free 到 unsorted bin<br>
     另外, 由於 calloc 不會從 tcache 拿 chunk , 所以 fastbin 的部份也得先填滿 tcache<br>
     填滿後 alloc 4 塊大小為 fastbin 的 chunk 再 alloc 一塊 unsorted bin 大小的 chunk<br>
     因為等等要 free 掉 unsorted bin chunk, 為了避免被 merge 到 top chunk, 所以還得再 alloc 一塊<br>
     以上 6 塊 chunk 下面依序用 0~5 號 chunk 替代<br>
     0 號 chunk 功能 : 修改 1 號 chunk 的 fd<br>
     3 號 chunk 功能 : 修改 4 號 chunk 的 size<br>
     首先, 我們把 2 號和 1 號 free 掉 (順序很重要)<br>
     因為我們只能預測 chunk addr 的最後一個 byte<br>
     所以欲修改的 fd 指到的位址只能跟 4 號的 addr 差一個 byte<br>
     而 2 號離 4 號較近, 所以讓 1 號的 fd 指到 2 號<br>
     接著修改修改 4 號的 size<br>
     再用 fastbin attack alloc 回來<br>
     再修改 4 號的 size 並 free 到 unsorted bin<br>
     最後再印出 2 號的內容, 就 leak 完成了<br>
     
   * <b>再修改 free_hook 成 system</b><br>
計算出 libc 位址後再用 fastbin attack 拿到 stdin+0x5 的位址<br>
為什麼是這個位址呢 ？<br>
因為我們是在 fastbin 操作, 跟 tcache 不同, bin 會檢查 size<br>
而從 free_hook 往上看 (一大片 \x00) 這個位址是最近的<br>
好在 fill 沒限制 size 所以可以瘋狂寫, 直到 free_hook<br>

   * <b> 最後再 free 掉內容為 /bin/sh 的 chunk</b>

* 後記
  * 為什麼不用 one_gadget 呢 ?<br>
因為參數(限制條件) 控不了

  * 這題當初是在 libc-2.19.so 下, 那個版本沒有 tcache 比較好做
     
