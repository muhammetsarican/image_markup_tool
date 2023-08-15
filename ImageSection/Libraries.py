import cv2, os, json, keyboard
from threading import Thread
import pyautogui

from ImageSection.Components import DrawGrid, RenewImage, GetSignedPictureCount, TakeFrame, ChangeImagePath, ChangeImagePath, GetBaseImage, SaveResizedImage, CloseUI, FindMarkedImages