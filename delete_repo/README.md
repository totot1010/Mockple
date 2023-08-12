# 手順
## GitHub CLI の alias登録
削除用のコマンドをaliasとして追加します。
```bash
gh alias set repo-delete 'api -X DELETE "repos/$1"'
```
また、権限を付与させるために以下のコマンドも実行させます。
```bash
gh auth refresh -h github.com -s delete_repo
```

## 実行する
```bash
bash delete_repo.sh
```

# 参考
https://dev.classmethod.jp/articles/git-hub-repo-delete/