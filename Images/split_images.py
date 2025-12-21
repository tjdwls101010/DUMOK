from PIL import Image
import os

def split_image_3x3(image_path, output_dir="split_images"):
    """
    이미지를 3x3 그리드로 분할하여 저장합니다.
    
    Args:
        image_path: 분할할 이미지 경로
        output_dir: 분할된 이미지를 저장할 디렉토리
    """
    # 출력 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 이미지 열기
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    # 각 조각의 크기 계산
    piece_width = img_width // 3
    piece_height = img_height // 3
    
    # 원본 파일명 추출 (확장자 제외)
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    
    print(f"처리 중: {base_name}")
    print(f"원본 크기: {img_width}x{img_height}")
    print(f"조각 크기: {piece_width}x{piece_height}")
    
    # 3x3 그리드로 분할
    for row in range(3):
        for col in range(3):
            # 각 조각의 좌표 계산
            left = col * piece_width
            upper = row * piece_height
            right = left + piece_width
            lower = upper + piece_height
            
            # 마지막 행/열의 경우 남은 픽셀 모두 포함
            if col == 2:
                right = img_width
            if row == 2:
                lower = img_height
            
            # 이미지 크롭
            cropped = img.crop((left, upper, right, lower))
            
            # 파일명 생성 및 저장
            output_filename = f"{base_name}_row{row+1}_col{col+1}.png"
            output_path = os.path.join(output_dir, output_filename)
            
            # PNG 형식으로 원본 화질 저장 (compress_level=0은 압축 없음)
            cropped.save(output_path, 'PNG', compress_level=0)
            print(f"  저장됨: {output_filename}")
    
    print()

def main():
    # 분할할 이미지 파일 목록
    image_files = [
        "nano-banana-1f027b76-d7f6-42f9-b6c1-1f4af0cac729.png",
        "nano-banana-70711666-bfa2-4dda-9823-d2d5147043be.png",
        "nano-banana-c6dfa5d7-128c-426a-8f23-14b169ea9faa.png",
        "nano-banana-da50a2b6-90c6-4939-ba70-9ae019fcdaf4.png"
    ]
    
    print("=" * 60)
    print("이미지 3x3 분할 시작")
    print("=" * 60)
    print()
    
    # 각 이미지 처리
    for image_file in image_files:
        if os.path.exists(image_file):
            split_image_3x3(image_file)
        else:
            print(f"경고: {image_file} 파일을 찾을 수 없습니다.")
    
    print("=" * 60)
    print("모든 이미지 분할 완료!")
    print("분할된 이미지는 'split_images' 폴더에 저장되었습니다.")
    print("=" * 60)

if __name__ == "__main__":
    main()

