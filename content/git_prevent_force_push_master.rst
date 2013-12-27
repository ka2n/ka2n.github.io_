masterへのforce pushとdeleteを防ぐpre-pushフック
============================================================================
:date: 2013-12-27
:author: ka2n
:tags: git
:category: dev
:summary: やるなと言われればそうなんだけど、対策する
:slug: git_prevent_force_push_master

やるな、と言われればそうなんだけど
うっかりmasterに ``git push --force`` とかやりそうになると背筋が凍る。
リモートがgithubだとリモート側で拒否とかできないので、クライアント側の ``pre-push`` フックを使って禁止したい。
調べてみると `良い感じ`_ なフックがあったので少しいじって使うことにした。

`.git/hooks/pre-push`

.. code-block:: sh
    
    protected_branches=( production master )
    for i in "${protected_branches[@]}"
    do
    
        protected_branch=$i
    
        policy='[Policy] Never push, force push or delete the '$protected_branch' branch! (Prevented with pre-push hook.)'
    
        current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
    
        push_command=$(ps -ocommand= -p $PPID)
    
        is_destructive='\-\-force|\-\-delete|\-f'
    
        will_remove_protected_branch=':'$protected_branch
    
        do_exit(){
          echo $policy
          exit 1
        }
    
        if [[ $push_command =~ $is_destructive ]] && [ $current_branch = $protected_branch ]; then
          do_exit
        fi
    
        if [[ $push_command =~ $is_destructive ]] && [[ $push_command =~ $protected_branch ]]; then
          do_exit
        fi
    
        if [[ $push_command =~ $will_remove_protected_branch ]]; then
          do_exit
        fi
    done
    
    unset do_exit
    
    exit 0
    

``protected_branches`` に列挙したブランチに

- ``git push --force``
- ``git push -f``
- ``git push --delete``
- ``git push :$branch``

なんてしようとした時に失敗してくれる。 便利だね。

.. _`良い感じ`: https://gist.github.com/pixelhandler/5718585
