# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['leach_win_setup.py'],
             pathex=['E:\\Ratul Codes\\C\\Python\\Web Leach\\Web-leach\\Web-leach_CLI\\v5'],
             binaries=[],
             datas=[('7z.exe', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='Web leach 0.5.5.4',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , version='vtesty.py', icon='EMO Angel.ico')
