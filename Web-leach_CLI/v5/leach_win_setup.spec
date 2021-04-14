# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\Ratul\\C\\Python\\Web Leach\\Web-leach\\Web-leach_CLI\\v5\\leach_win_setup.py'],
             pathex=['D:\\Ratul\\C\\Python\\Web Leach\\Web-leach\\Web-leach_CLI\\v5'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='leach_win_setup',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
